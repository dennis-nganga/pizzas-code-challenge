from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class Pizza(db.Model):
    __tablename__ = 'pizzas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant_pizzas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))

    pizza = db.relationship('Pizza', backref='restaurant_pizzas')

