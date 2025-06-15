# 🍕 Pizza API

A simple Flask REST API for managing restaurants, pizzas, and their associations.

---

## ⚙️ Setup Instructions

```bash
# Clone the repo and navigate into it
git clone https://github.com/Jerome-Chauncey/pizza-api-challenge.git
cd pizza-api-challenge

# Create and activate virtual environment
pipenv install
pipenv shell

# Set up the database
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

# Seed the database
PYTHONPATH=. python server/seed.py

# Run the app
PYTHONPATH=. python server/app.py


## 🗂 Route Summary

| Method | Route                | Description                    |
|--------|----------------------|--------------------------------|
| GET    | /restaurants         | Get all restaurants            |
| GET    | /restaurants/:id     | Get one restaurant with pizzas |
| DELETE | /restaurants/:id     | Delete a restaurant            |
| GET    | /pizzas              | Get all pizzas                 |
| POST   | /restaurant_pizzas   | Create a restaurant-pizza link |



🧪 Example Requests & Responses
➕ GET /restaurants
Response:

[
  {
    "id": 1,
    "name": "Luigi's Pizza",
    "address": "123 Main St"
  }
]
➕ GET /restaurants/1
Response:

{
  "id": 1,
  "name": "Luigi's Pizza",
  "address": "123 Main St",
  "pizzas": [
    {
      "id": 1,
      "name": "Margherita",
      "ingredients": "Tomato, Mozzarella, Basil"
    }
  ]
}
➕ POST /restaurant_pizzas
Request:

{
  "price": 15,
  "pizza_id": 1,
  "restaurant_id": 2
}
Response:

{
  "id": 4,
  "price": 15,
  "pizza": {
    "id": 1,
    "name": "Margherita",
    "ingredients": "Tomato, Mozzarella, Basil"
  }
}
❌ DELETE /restaurants/1
Response:
{}



✅ Validation Rules
price must be between 1 and 30

restaurant_id and pizza_id must exist in the database

🧪 Using Postman
Open Postman

Manually test the routes and don't forget to run app.py


