# app/sites/cart.py

import streamlit as st

from src.layout import setup_layout
from components.cart import render_cart
from components.shipping import render_shipping

setup_layout(page_title='Checkout - Flapp')

if 'cart' not in st.session_state or not st.session_state.cart:
    st.warning('Cart not found. Please generate one first.')
    if st.button('↩️ Back to Home'):
        st.switch_page('sites/home.py')
    st.stop()

col_1, col_2 = st.columns([0.3, 0.7])

with col_1:

    render_shipping()
    st.divider()
    col_a, col_b = st.columns(2)

    with col_a:
        if st.button('🔄 Clear Cart'):
            st.session_state.cart = None
            st.session_state.shipping = None
            st.switch_page('sites/home.py')

    with col_b:
        if st.button('↩️ Back'):
            st.switch_page('sites/home.py')

with col_2:
    render_cart()
