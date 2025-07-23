# app/components/cart.py

import streamlit as st

import pandas as pd

def render_cart():
    """Render the shopping cart details including product list and summary."""
    cart = st.session_state.cart
    if not cart or 'products' not in cart:
        st.warning('Cart is empty or invalid.')
        return

    _render_table(cart)
    _render_summary(cart)

def _render_table(cart: dict):
    st.subheader(f'🧾 Cart Summary (ID: {cart["id"]})')
    df = pd.DataFrame(cart['products']).rename(columns={
        'title': 'Product',
        'price': 'Unit Price',
        'quantity': 'Quantity',
        'discountPercentage': 'Discount (%)',
        'discountedTotal': 'Total (after discount)',
    })
    st.dataframe(
        df[['Product', 'Unit Price', 'Quantity', 'Discount (%)', 'Total (after discount)']],
        use_container_width=True
    )

def _render_summary(cart: dict):
    st.markdown(f"""
        <div style="margin-top: 1.5rem; padding: 1rem 1.5rem; border: 1px solid #ddd;
                    border-radius: 10px; background-color: #f9f9f9;">
            <h4 style="margin-bottom: 0.75rem;">🧮 <u>Cart Summary Details</u></h4>
            <ul style="list-style: none; padding-left: 0; font-size: 15px; line-height: 1.6;">
                <li>🛍 <strong>Total Products:</strong> {cart["totalProducts"]}</li>
                <li>🔢 <strong>Total Quantity:</strong> {cart["totalQuantity"]}</li>
                <li>💰 <strong>Original Total:</strong> ${cart["total"]:.2f}</li>
                <li>💸 <strong>Discounted Total:</strong>
                    <span style="color: #009e60; font-weight: bold;">
                        ${cart["discountedTotal"]:.2f}
                    </span>
                </li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
