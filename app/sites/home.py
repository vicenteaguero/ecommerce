# app/sites/home.py

import streamlit as st

import requests
import random

from src.params import DUMMY_CART_URL
from src.layout import setup_layout

setup_layout(page_title='Home - E-Commerce')

st.title('Welcome to E-Commerce Simulator')
st.write('Simulate a full shopping flow by generating a cart and proceeding to checkout.')

if 'cart' not in st.session_state:
    st.session_state.cart = None

col1, col2 = st.columns([0.4, 0.6])

with col1:
    if st.button('🎲 Generate Random Cart'):
        r = requests.get(f'{DUMMY_CART_URL}/{random.randint(1, 50)}')
        if r.status_code == 200:
            st.session_state.cart = r.json()
            st.success('Cart loaded successfully!')
            st.info('➡️ Go to **🛒 Shopping Cart** from the sidebar to continue.')
        else:
            st.error('Failed to load cart. Please try again.')

with col2:
    if st.session_state.cart:
        st.success('Cart is ready.')
        st.info('✅ You can now navigate to **🛒 Shopping Cart** from the sidebar.')
    else:
        st.warning('No cart loaded yet. Please generate one.')
