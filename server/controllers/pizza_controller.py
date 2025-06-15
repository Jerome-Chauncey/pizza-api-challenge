from flask import jsonify
from server.models.pizza import Pizza

def get_all_pizzas():
    pizzas = Pizza.query.all()
    return jsonify([p.to_dict() for p in pizzas]), 200
