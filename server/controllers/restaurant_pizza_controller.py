from flask import request, jsonify
from server.models.restaurant_pizza import RestaurantPizza
from server.models import db

def create_restaurant_pizza():
    data = request.get_json()

    try:
        price = int(data.get("price"))
        pizza_id = data.get("pizza_id")
        restaurant_id = data.get("restaurant_id")

        if price < 1 or price > 30:
            raise ValueError("Price must be between 1 and 30")

        rp = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
        db.session.add(rp)
        db.session.commit()

        return jsonify(rp.to_dict(include_related=True)), 201

    except Exception as e:
        return jsonify({"errors": [str(e)]}), 400
    


