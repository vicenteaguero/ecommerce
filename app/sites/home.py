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

btn_clicked = st.button('🎲 Generate Random Cart')

if btn_clicked:
    r = requests.get(f'{DUMMY_CART_URL}/{random.randint(1, 50)}')
    if r.ok:
        st.session_state.cart = r.json()
        st.success('✅ Cart loaded and ready.')
        st.info('➡️ Go to **🛒 Shopping Cart** from the sidebar to continue.')
    else:
        st.error('❌ Failed to load cart. Please try again.')

if not btn_clicked and not st.session_state.cart:
    st.warning('No cart loaded yet. Please generate one.')
