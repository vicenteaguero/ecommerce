# app/src/layout.py

import streamlit as st

from src.params import PATHS, GITHUB_URL, REPORT_URL_MAIL, ABOUT_TEXT

def setup_layout(page_title: str):
    """Set up the layout of the Streamlit app."""
    st.set_page_config(
        layout='wide',
        page_title=page_title,
        page_icon=PATHS['favicon'],
        initial_sidebar_state='expanded',
        menu_items={
            'Get Help': GITHUB_URL,
            'Report a bug': REPORT_URL_MAIL,
            'About': ABOUT_TEXT,
        },
    )

    st.logo(
        image=PATHS['logo'],
        link=GITHUB_URL,
    )
    st.markdown("""
        <style>
            img.stLogo {display: block; height: 50px; margin: 0}
        </style>
    """, unsafe_allow_html=True)

def setup_pages():
    """
    Set up the pages of the Streamlit app.

    Returns
    -------
    None
    """
    pages = {
        'General': [
            st.Page(
                page=PATHS['pages']['home'],
                title='Home',
                icon='🏠',
            ),
            st.Page(
                page=PATHS['pages']['docs'],
                title='Documentation',
                icon='📚',
            ),
        ],
        'Features': [
            st.Page(
                page=PATHS['pages']['cart'],
                title='Shopping Cart',
                icon='🛒',
            ),
        ],
    }

    pg = st.navigation(pages)
    pg.run()
