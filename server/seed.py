from server.extensions import db
from sqlalchemy import text
from server.app import create_app
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

app = create_app()

with app.app_context():
    
    db.session.query(RestaurantPizza).delete()
    db.session.query(Restaurant).delete()
    db.session.query(Pizza).delete()

   
    db.session.execute(text("ALTER SEQUENCE restaurant_pizzas_id_seq RESTART WITH 1"))
    db.session.execute(text("ALTER SEQUENCE restaurants_id_seq RESTART WITH 1"))
    db.session.execute(text("ALTER SEQUENCE pizzas_id_seq RESTART WITH 1"))

   
    pizza1 = Pizza(name="Margherita", ingredients="Tomato, Mozzarella, Basil")
    pizza2 = Pizza(name="Pepperoni", ingredients="Tomato, Mozzarella, Pepperoni")

    r1 = Restaurant(name="Luigi's Pizza", address="123 Main St")
    r2 = Restaurant(name="Mario's Pies", address="456 Side St")

    rp1 = RestaurantPizza(price=10, restaurant=r1, pizza=pizza1)
    rp2 = RestaurantPizza(price=12, restaurant=r1, pizza=pizza2)
    rp3 = RestaurantPizza(price=15, restaurant=r2, pizza=pizza1)

    db.session.add_all([pizza1, pizza2, r1, r2, rp1, rp2, rp3])
    db.session.commit()

    print("Db seeded!")
