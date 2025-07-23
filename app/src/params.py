# app/src/params.py

import os

################################################################################

# Basic Parameters

APP_NAME = 'app'

# App Folders
PAGES_FOLDER = 'sites'
ASSETS_FOLDER = 'assets'

# App Logo
LOGO_FILE = 'logo.png'
FAVICON_FILE = 'favicon.png'

# About Info
README_ABOUT = 'ABOUT.md'
GITHUB_URL = 'https://github.com/vicenteaguero/ecommerce'
REPORT_URL_MAIL = 'mailto:vicenteaguero@uc.cl'

# API URL
API_URL = 'http://localhost:8000/api/cart'

################################################################################

# Root Paths

BASE_DIR = os.path.join(os.path.dirname(__file__), '..', '..')
APP_DIR = os.path.join(BASE_DIR, APP_NAME)

# App Paths

ASSETS_DIR = os.path.join(APP_DIR, ASSETS_FOLDER)
PAGES_DIR = os.path.join(APP_DIR, PAGES_FOLDER)

# Paths

PATHS = {
    'logo': os.path.join(ASSETS_DIR, LOGO_FILE),
    'favicon': os.path.join(ASSETS_DIR, FAVICON_FILE),
    'about': os.path.join(APP_DIR, README_ABOUT),
    'pages': {
        os.path.splitext(x)[0]: os.path.join(PAGES_DIR, x) for x in os.listdir(PAGES_DIR)
    },
}

################################################################################

# About Text
with open(PATHS['about']) as f:
    ABOUT_TEXT = f.read()

################################################################################

# API URLs

API_CART_URL = f'{API_URL}/api/cart'