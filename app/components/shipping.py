# app/components/shipping.py

import streamlit as st
import requests

from src.params import API_CART_URL

def render_shipping():
    """Render the shipping form and handle shipping quote requests."""
    _render_form()
    _render_actions()

def _render_form():
    st.session_state.setdefault('shipping', {})
    shipping = st.session_state.shipping or {}
    st.session_state.shipping = {
        'name': st.text_input('Name', value=shipping.get('name', '')),
        'shipping_street': st.text_input('Street', value=shipping.get('shipping_street', '')),
        'commune': st.text_input('Commune', value=shipping.get('commune', '')),
        'phone': st.text_input('Phone', value=shipping.get('phone', '+569')),
    }

def _render_actions():
    if st.button('📦 Quote Shipping'):
        data = {
            'products': [
                {
                    'product_id': p['id'],
                    'price': p['price'],
                    'quantity': p['quantity'],
                    'discount': p['discountPercentage'],
                } for p in st.session_state.cart['products']
            ],
            'customer_data': st.session_state.shipping,
        }
        try:
            r = requests.post(API_CART_URL, json=data)
            if r.ok:
                res = r.json()
                st.success(f"🚚 Shipping with **{res['courier']}** - ${res['price']:,.0f}")
            else:
                st.error('❌ No available shipping options')
        except Exception:
            st.error('⚠️ Failed to contact backend')

    if st.button('🧹 Clear Cart'):
        st.session_state.cart = None
        st.session_state.shipping = None
