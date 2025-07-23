# api/src/params.py

from dotenv import load_dotenv

import os

################################################################################

# Base Paths

BASE_DIR = os.path.join(os.path.dirname(__file__), '..', '..')
ETC_DIR = os.path.join(BASE_DIR, 'etc')

# Load .env

load_dotenv(os.path.join(ETC_DIR, '.env'))

# External URLs

DUMMY_PRODUCTS_URL = 'https://dummyjson.com/products'
TRAELOYA_URL = 'https://recruitment.weflapp.com/tarifier/traelo_ya'
UDER_URL = 'https://recruitment.weflapp.com/tarifier/uder'

# API Keys

TRAELOYA_API_KEY = os.getenv('TRAELOYA_API_KEY', 'demo-traelo')
UDER_API_KEY = os.getenv('UDER_API_KEY', 'demo-uder')

# Origin Information

ORIGIN = {
    'name':     'Tienda Flapp',
    'phone':    '+56912345678',
    'street':   'Juan de Valiente 3630',
    'commune':  'Vitacura',
}
