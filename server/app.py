from flask import Flask
from server.controllers.restaurant_controller import get_all_restaurants, get_restaurant_by_id, delete_restaurant
from server.controllers.pizza_controller import get_all_pizzas
from server.controllers.restaurant_pizza_controller import create_restaurant_pizza

from server.config import Config
from server.extensions import db, migrate


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from server.models import restaurant, pizza, restaurant_pizza

    @app.route("/restaurants", methods=["GET"])
    def restaurants():
        return get_all_restaurants()

    @app.route("/restaurants/<int:id>", methods=["GET"])
    def restaurant_detail(id):
        return get_restaurant_by_id(id)

    @app.route("/restaurants/<int:id>", methods=["DELETE"])
    def delete_restaurant_route(id):
        return delete_restaurant(id)

    @app.route("/pizzas", methods=["GET"])
    def pizzas():
        return get_all_pizzas()

    @app.route("/restaurant_pizzas", methods=["POST"])
    def create_rp():
        return create_restaurant_pizza()

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
