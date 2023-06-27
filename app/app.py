#!/usr/bin/env python3

from flask import Flask
from flask_migrate import Migrate
from models import db, Restaurant, Pizza, RestaurantPizza
from flask import jsonify

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)



@app.route('/Home')
def home():
    return '<h2>Flask app for Restaurants</h2>'

@app.route('/restaurants')
def get_restaurants():
    restaurants = Restaurant.query.all()
    restaurant_list = []
    for restaurant in restaurants:
        restaurant_info = {
            'id': restaurant.id,
            'name': restaurant.name,
            'pizzas': [pizza.name for pizza in restaurant.pizzas]
        }
        restaurant_list.append(restaurant_info)
    return jsonify(restaurant_list)

@app.route('/pizzas')
def get_pizzas():
    pizzas = Pizza.query.all()
    pizza_list = []
    for pizza in pizzas:
        pizza_info = {
            'id': pizza.id,
            'name': pizza.name,
            'price': pizza.price,
            'created_at': pizza.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }
        pizza_list.append(pizza_info)
    return jsonify(pizza_list)

if __name__ == '__main__':
  app.run(port=5501, debug=True)