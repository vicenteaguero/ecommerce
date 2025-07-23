# app/src/layout.py

import streamlit as st

from src.params import PATHS, GITHUB_URL, REPORT_URL_MAIL, ABOUT_TEXT

def setup_layout(page_title: str):
    """Set up the Streamlit layout with custom configurations."""
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
    st.logo(image=PATHS['logo'], link=GITHUB_URL)
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');

            @font-face {
                font-family: 'Averta';
                src: url('https://raw.githubusercontent.com/google/fonts/main/ofl/sourcesanspro/SourceSansPro-Regular.ttf') format('truetype');
                font-weight: 400;
                font-style: normal;
                font-display: swap;
            }

            html, body, [class*="css"] {
                font-family: 'Averta', sans-serif !important;
            }

            img.stLogo {
                display: block;
                width: 100%;
                height: auto;
                margin-top: 20px;
            }
        </style>
    """, unsafe_allow_html=True)

def setup_pages():
    """Set up the navigation pages for the Streamlit app."""
    pages = {
        'General': [
            st.Page(page=PATHS['pages']['home'], title='Home', icon='🏠'),
            st.Page(page=PATHS['pages']['docs'], title='Documentation', icon='📚'),
        ],
        'Features': [
            st.Page(page=PATHS['pages']['cart'], title='Shopping Cart', icon='🛒'),
        ],
    }
    st.navigation(pages).run()
