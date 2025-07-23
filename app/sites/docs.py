# app/sites/docs.py

import streamlit as st
from src.layout import setup_layout

setup_layout(page_title='Documentation - Flapp Simulator')

st.title('Flapp Simulator – Documentation')

st.markdown('## 🎮 How to use the web app')

st.markdown("""
1. **Home**  
   • Click **🎲 Generate Random Cart** to pull a sample cart from DummyJSON.  
   • When loaded, navigate to **🛒 Shopping Cart** from the sidebar.

2. **Shopping Cart**  
   • Review items and totals.  
   • Fill **Name, Street, Commune, Phone** in the left‑hand form.  
   • Click **📦 Quote Shipping** to retrieve real‑time courier prices.  
   • Lowest quote is displayed → _“Shipping with TraeloYa – $5 990”_.  
   • **🧹 Clear Cart** resets everything; **↩️ Back** returns to Home.

3. **State management**  
   • Cart is stored in `st.session_state.cart`.  
   • Shipping data persists in `st.session_state.shipping`.  
   • Clearing the cart wipes both keys.
""")

st.markdown('---')
st.markdown('## 🔌 API reference')

st.markdown('### Endpoint')
st.code('POST /api/cart', language='bash')

st.markdown('### Request JSON schema')
st.code("""{
  "products": [
    {
      "productId": 1,
      "price": 49.99,
      "quantity": 2,
      "discount": 5
    }
  ],
  "customer_data": {
    "name": "Juan Pérez",
    "shipping_street": "Calle Falsa 123",
    "commune": "Vitacura",
    "phone": "+56912345678"
  }
}""", language='json')

st.markdown('### Response')
st.code("""{
  "courier": "TraeloYa",
  "price": 5990.0
}""", language='json')

st.markdown('### Curl demo')
st.code("""curl -X POST http://localhost:8000/api/cart \\
  -H "Content-Type: application/json" \\
  -d @payload.json""", language='bash')

st.markdown('### Error responses')
st.code('400  Insufficient real stock for: 3, 7', language='')

st.markdown('### FastAPI interactive docs')
st.markdown('- Local: [http://localhost:8000/docs](http://localhost:8000/docs)')

st.markdown('---')
st.markdown('## 🚚 Courier integration')

st.markdown("""
| Courier | URL | Header |
|---------|-----|--------|
| TraeloYa | https://recruitment.weflapp.com/tarifier/traelo_ya | `X-Api-Key: $TRAELOYA_API_KEY` |
| Uder | https://recruitment.weflapp.com/tarifier/uder | `X-Api-Key: $UDER_API_KEY` |

The backend requests both couriers in parallel, picks the cheapest quote, and returns it to the frontend.
""")

st.markdown('### Quick local test (cURL)')
st.code("""\
curl -X POST http://localhost:8000/api/cart \
     -H "Content-Type: application/json" \
     -d '{"products":[{"productId":1,"price":49.99,"quantity":2,"discount":5}],\
          "customer_data":{"name":"Juan Pérez","shipping_street":"Calle Falsa 123",\
          "commune":"Vitacura","phone":"+56912345678"}}'
""", language='bash')

st.markdown("""
> **Nota:** para que este request funcione con los couriers reales debes definir  
> `TRAELOYA_API_KEY` y `UDER_API_KEY` en tu archivo **`etc/.env`**:
>
> ```env
> TRAELOYA_API_KEY=tu_clave_traeloya
> UDER_API_KEY=tu_clave_uder
> ```
>
> Luego inicia el backend con:
>
> ```bash
> poetry run uvicorn api.main:app --reload
> ```
""")
