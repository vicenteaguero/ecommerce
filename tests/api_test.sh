#!/bin/bash

URL="http://localhost:8000/api/cart"

read -r -d '' DATA <<EOF
{
  "products": [
    { "productId": 1, "price": 49.99, "quantity": 1, "discount": 5 },
    { "productId": 5, "price": 29.99, "quantity": 2, "discount": 0 }
  ],
  "customer_data": {
    "name": "Vicente Agüero",
    "shipping_street": "Juan de Valiente 3630",
    "commune": "Vitacura",
    "phone": "+56912345678"
  }
}
EOF

curl -s -X POST "$URL" \
  -H "Content-Type: application/json" \
  -d "$DATA" \
  | jq
