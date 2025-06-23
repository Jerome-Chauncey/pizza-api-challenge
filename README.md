# 🍕 Pizza Restaurant API

A Flask-based REST API for managing pizza restaurants, their menus, and pizza offerings.

---

## 🛠️ Setup

### Prerequisites

* Python 3.10+
* PostgreSQL (or SQLite for development)
* Pipenv

### Installation

```bash
# Clone the repository
git clone https://github.com/Jerome-Chauncey/pizza-api-challenge.git
cd pizza-api-challenge

# Install dependencies and activate environment
pipenv install
pipenv shell
```

---

## 🗄️ Database Setup

1. **Configuration**
   Update `server/config.py` with your database URI:

   ```python
   SQLALCHEMY_DATABASE_URI = 'postgresql://dbadmin:your_password@localhost/pizza_restaurant'
   # or for SQLite:
   # SQLALCHEMY_DATABASE_URI = 'sqlite:///pizza.db'
   ```

2. **Migrations**
   Initialize and apply database migrations:

   ```bash
   export FLASK_APP=server/app.py
   flask db init
   flask db migrate -m "initial migration"
   flask db upgrade
   ```

3. **Seeding Data**
   Populate the database with sample data:

   ```bash
   python server/seed.py
   ```

---

## 🌐 API Routes

### Restaurants

| Method | Endpoint            | Description                  |
| ------ | ------------------- | ---------------------------- |
| GET    | `/restaurants`      | Retrieve all restaurants     |
| GET    | `/restaurants/<id>` | Retrieve a single restaurant |
| DELETE | `/restaurants/<id>` | Delete a restaurant          |

### Pizzas

| Method | Endpoint  | Description         |
| ------ | --------- | ------------------- |
| GET    | `/pizzas` | Retrieve all pizzas |

### Restaurant Pizzas

| Method | Endpoint             | Description                           |
| ------ | -------------------- | ------------------------------------- |
| POST   | `/restaurant_pizzas` | Create a restaurant-pizza association |

---

## 📝 Example Requests & Responses

### Get All Restaurants

**Request**

```http
GET /restaurants
```

**Response**

```json
[
  {
    "id": 1,
    "name": "Pizza Palace",
    "address": "123 Main St"
  }
]
```

### Create Restaurant Pizza

**Request**

```http
POST /restaurant_pizzas
Content-Type: application/json

{
  "price": 10,
  "pizza_id": 1,
  "restaurant_id": 1
}
```

**Success Response (201)**

```json
{
  "id": 1,
  "price": 10,
  "pizza": { "id": 1, "name": "Cheese" },
  "restaurant": { "id": 1, "name": "Pizza Palace" }
}
```

**Error Response (400)**

```json
{
  "errors": ["Price must be between 1 and 30"]
}
```

---

## ✅ Validation Rules

* **price**: Must be between 1 and 30
* **pizza\_id**: Must reference an existing pizza
* **restaurant\_id**: Must reference an existing restaurant

---

## 🚀 Running the Server

```bash
# From project root
python -m server.app
# Or from server directory
PYTHONPATH=.. python app.py
```

---

## 📮 Postman Testing

1. **Import the Collection**

   * Open Postman, click **Import**, select `challenge-1-pizzas.postman_collection.json`.

2. **Set Environment Variables**

   * `base_url`: `http://localhost:5000`

3. **Test Endpoints**

   * Execute all routes in the collection and verify responses.

---

## 📦 Dependencies

* Flask 3.1.1
* Flask-SQLAlchemy 3.1.1
* Flask-Migrate 4.1.0
* psycopg2-binary 2.9.10 (for PostgreSQL)
* SQLAlchemy 2.0.41

---

## 🔗 GitHub Repository

[https://github.com/Jerome-Chauncey/pizza-api-challenge](https://github.com/Jerome-Chauncey/pizza-api-challenge)
