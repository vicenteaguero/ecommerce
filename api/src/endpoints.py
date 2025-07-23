# api/src/endpoints.py

import asyncio
import logging
import math

import httpx
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from api.src.params import (
    DUMMY_PRODUCTS_URL, ORIGIN, TRAELOYA_URL, TRAELOYA_API_KEY, UDER_URL, UDER_API_KEY,
)
from api.src.schemas import CartRequest, QuoteOut

router = APIRouter()

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

async def _fetch_page(client: httpx.AsyncClient, skip: int, limit: int = 10) -> dict:
    """Fetch a single page of products from the dummy API."""
    r = await client.get(f'{DUMMY_PRODUCTS_URL}?limit={limit}&skip={skip}')
    r.raise_for_status()
    return r.json()

async def fetch_all_products() -> dict[int, dict]:
    """Fetch all products from the dummy API and return a dictionary of products."""
    async with httpx.AsyncClient(timeout=5) as c:
        first = await _fetch_page(c, 0)
        total = first['total']
        pages = await asyncio.gather(*[_fetch_page(c, s) for s in range(0, total, 10)])
    return {p['id']: p for page in pages for p in page['products']}

def real_stock(stock: int, rating: float) -> int:
    """Calculate the real stock based on the product rating."""
    return math.floor(stock / rating) if rating else 0

async def quote_traeloya(dest: dict, items: list[dict]) -> float | None:
    """Get shipping quote from TraeloYa."""
    headers = {'X-Api-Key': TRAELOYA_API_KEY}
    payload = {
        'items': [
            {
                'quantity': i['quantity_req'],
                'value': float(i['unit_price']),
                'volume': i['volume'],
            }
            for i in items
        ],
        'waypoints': [
            {
                'type': 'PICK_UP',
                'addressStreet': ORIGIN['street'],
                'city': ORIGIN['commune'],
                'phone': ORIGIN['phone'],
                'name': ORIGIN['name'],
            },
            {
                'type': 'DROP_OFF',
                'addressStreet': dest['street'],
                'city': dest['commune'],
                'phone': dest['phone'],
                'name': dest['name'],
            },
        ],
    }

    async with httpx.AsyncClient(timeout=5) as c:
        r = await c.post(TRAELOYA_URL, json=payload, headers=headers)

    if r.status_code != 200:
        return None

    data = r.json()

    if 'deliveryOffers' not in data:
        return None

    return float(data['deliveryOffers']['pricing']['total'])

async def quote_uder(dest: dict, items: list[dict]) -> float | None:
    """Get shipping quote from Uder."""
    headers = {'X-Api-Key': UDER_API_KEY}
    payload = {
        'pickup_address': ORIGIN['street'],
        'pickup_name': ORIGIN['name'],
        'pickup_phone_number': ORIGIN['phone'],
        'dropoff_address': dest['street'],
        'dropoff_name': dest['name'],
        'dropoff_phone_number': dest['phone'],
        'manifest_items': [
            {
                'name': i['name'],
                'quantity': i['quantity_req'],
                'price': float(i['unit_price']),
                'dimensions': i['dimensions'],
            }
            for i in items
        ],
    }

    async with httpx.AsyncClient(timeout=5) as c:
        r = await c.post(UDER_URL, json=payload, headers=headers)

    if r.status_code != 200:
        return None

    data = r.json()

    return float(data['fee']) if 'fee' in data else None

async def gather_quotes(dest: dict, items: list[dict]) -> list[QuoteOut]:
    """Gather quotes from both couriers and return a list of QuoteOut."""
    t, u = await asyncio.gather(quote_traeloya(dest, items), quote_uder(dest, items))
    quotes = list()
    if t:
        quotes.append(QuoteOut(courier='TraeloYa', price=t))
    if u:
        quotes.append(QuoteOut(courier='Uder', price=u))
    return quotes

@router.post('', response_model=QuoteOut)
async def create_cart(cart: CartRequest):
    """Create a shopping cart and return the best shipping quote."""
    catalog = await fetch_all_products()
    enriched = list()

    for p in cart.products:
        prod = catalog.get(p.product_id)
        if not prod:
            raise HTTPException(400, f'Product {p.product_id} not found')
        sr = real_stock(prod['stock'], prod['rating'])
        raw_dims = prod.get('dimensions', {})
        length = raw_dims.get('length') or raw_dims.get('width') or 1
        height = raw_dims.get('height', 1)
        depth = raw_dims.get('depth', 1)
        dims = {'length': length, 'height': height, 'depth': depth}
        vol = length * height * depth
        enriched.append({
            'id': p.product_id,
            'name': prod['title'],
            'unit_price': p.price,
            'discount': p.discount,
            'quantity_req': p.quantity,
            'stock': prod['stock'],
            'rating': prod['rating'],
            'stock_real': sr,
            'dimensions': dims,
            'volume': vol,
        })
    logger.info(f'📦 Cart received with {len(enriched)} products:')
    for p in enriched:
        logger.info(
            f"ID {p['id']:>3} | {p['name']:<30} | ${p['unit_price']:>6.2f} | "
            f"Desc {p['discount']:>4} | Qty {p['quantity_req']:>2} | "
            f"Stock {p['stock']:>3} | R {p['rating']:.1f} | Sr {p['stock_real']:>3}"
        )

    lacks = [e for e in enriched if e['quantity_req'] > e['stock_real']]
    if lacks:
        ids = ', '.join(str(e['id']) for e in lacks)
        raise HTTPException(400, f'Insufficient real stock for: {ids}')

    dest = {
        'name': cart.customer_data.name,
        'phone': cart.customer_data.phone,
        'street': cart.customer_data.shipping_street,
        'commune': cart.customer_data.commune,
    }

    quotes = await gather_quotes(dest, enriched)
    if not quotes:
        raise HTTPException(400, 'No courier quotes available')

    best = min(quotes, key=lambda q: q.price)

    return JSONResponse(best.dict())
