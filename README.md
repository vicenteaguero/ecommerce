# 🛍️ E-Commerce Simulator

[![Streamlit App](https://img.shields.io/badge/Live_App-Streamlit-FF4B4B)](https://ecommerce-flapp.streamlit.app/)

Simulador interactivo de compras que combina un frontend visual en Streamlit con un backend en FastAPI para cotizar despachos vía couriers ficticios. El sistema integra productos desde una API pública (`dummyjson.com`) y permite experimentar con flujos completos de checkout, cálculo de stock real, y tarifas de envío.

---

## 🧠 Funcionalidades

- 🛒 Generación aleatoria de carritos desde una API externa
- 🧾 Visualización detallada del carrito y resumen de compra
- 🚚 Cotización de despacho con **TraeloYa** y **Uder**
- 🧮 Cálculo de stock real en base a rating del producto
- 🧼 Limpieza de carrito y retorno al flujo inicial
- 🌐 Interfaz oscura personalizada, con tipografía *Averta*

---

## 🚀 Demo Online

🔗 **[Abrir la App →](https://ecommerce-flapp.streamlit.app/)**  
(Sin necesidad de instalación)

---

## 🖥️ Instrucciones de uso local

### 1. Requisitos

* Python 3.10+
* [`poetry`](https://python-poetry.org/docs/#installation)

### 2. Clonar el repositorio

```bash
git clone https://github.com/tuusuario/ecommerce-simulator.git
cd ecommerce-simulator
```

### 3. Crear archivo `.env`

```env
# etc/.env
TRAELOYA_API_KEY=your_real_key
UDER_API_KEY=your_real_key
```

(O puedes dejar los valores por defecto `demo-traelo` y `demo-uder` para pruebas.)

### 4. Instalar dependencias

```bash
poetry install --no-dev
```

> Si usas entorno virtual administrado por Poetry, puedes activarlo con:
>
> ```bash
> poetry shell
> ```

### 5. Ejecutar el backend (API)

```bash
poetry run uvicorn api.main:app --reload
```

Esto iniciará el backend en: [http://localhost:8000](http://localhost:8000)

### 6. Ejecutar el frontend (Streamlit)

```bash
poetry run streamlit run app/app.py
```

Esto abrirá la app en: [http://localhost:8501](http://localhost:8501)

---

## 🐳 Docker (Recomendado)

### Ejecutar toda la app (API + Frontend):

```bash
docker compose up --build
```

* Frontend: [http://localhost:8501](http://localhost:8501)
* API Docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🔁 Ejemplo de API Request

```bash
curl -X POST http://localhost:8000/api/cart \
     -H "Content-Type: application/json" \
     -d '{"products":[{"productId":1,"price":49.99,"quantity":2,"discount":5}],
          "customer_data":{"name":"Juan Pérez","shipping_street":"Calle Falsa 123",
          "commune":"Vitacura","phone":"+56912345678"}}'
```

---

## 📦 Estructura del Proyecto

```
.
├── api/                  # Backend FastAPI
├── app/                  # Frontend Streamlit
├── etc/.env              # Variables de entorno
├── docker-compose.yml
├── pyproject.toml
```

---

## 📄 Documentación Técnica

Consulta la sección **📚 Documentation** dentro de la app para más detalles sobre:

* Flujo del sistema
* Estructura del endpoint `/api/cart`
* Formato esperado para couriers ficticios
* Validaciones y lógica de stock

---

## ✅ Supuestos realizados

* Se considera "stock real" como `stock // rating` (entero)
* Envío falla si no hay stock suficiente para todos los productos
* Si ningún courier cotiza, se retorna error 400
