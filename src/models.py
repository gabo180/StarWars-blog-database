from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=False, nullable=False)
    first_name = db.Column(db.String(120), unique= False, nullable=False)
    last_name = db.Column(db.String(120), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)
    # password = db.Column(db.String(80), unique=False, nullable=False)
    favorite_planets = db.relationship("Favorite", back_populates="planet")

    def to_dict(self):
        return {
        '<user %s>' % self.user
        }


    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Favorite(db.Model):
    __tablename__ = 'favorite'
    user_id = db.Column(db.ForeignKey('user.id'), primary_key=True)
    planet_id = db.Column(db.ForeignKey('planet.id'), primary_key=True)
    character_id = db.Column(db.ForeignKey('character.id'), primary_key=True)
    vehicle_id = db.Column(db.ForeignKey('vehicle.id'), primary_key=True)
    user = db.relationship("Planet", back_populates="users")
    planet = db.relationship("User", back_populates="favorite_planets")

    def to_dict(self):
        return {
        '<favorite %s>' % self.favorite
        }


    def serialize(self):
        return {
            "character_id": self.character_id,
            "vehicle_id": self.vehicle_id,
            "planet_id": self.planet_id,
            "user_id": self.user_id
        }
class Character(db.Model):
    __tablename__ = 'character'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    height = db.Column(db.String(120), unique=False, nullable=False)
    hair_color = db.Column(db.String(120), unique=False, nullable=False)
    eye_color = db.Column(db.String(120), unique=False, nullable=False)
    birth_year = db.Column(db.String(120), unique=False, nullable=False)
    gender = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return '<character %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "hair_color": self.hair_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender
        }

class Planet(db.Model):
    __tablename__ = 'planet'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    population = db.Column(db.Integer, unique=False, nullable=False)
    terrain = db.Column(db.String(120), unique=False, nullable=False)
    climate = db.Column(db.String(120), unique=False, nullable=False)
    diameter = db.Column(db.Integer, unique=False, nullable=False)
    gravity = db.Column(db.String(120), unique=False, nullable=False)
    users = db.relationship("Favorite", back_populates="user")

    def to_dict(self):
        return {
        '<planet %s>' % self.planet
        }


    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population,
            "terrain": self.terrain,
            "gravity": self.gravity,
            "climate": self.climate,
            "diameter": self.diameter
        }

class Vehicle(db.Model):
    __tablename__ = 'vehicle'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    model = db.Column(db.String(120), unique=False, nullable=False)
    manufaturer = db.Column(db.String(120), unique=False, nullable=False)
    cost_in_credits = db.Column(db.Integer, unique=False, nullable=False)
    cargo_capacity = db.Column(db.Integer, unique=False, nullable=False)
    vehicle_class = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return '<vehicle %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "manufaturer": self.manufaturer,
            "cost_in_credits": self.cost_in_credits,
            "cargo_capacity": self.cargo_capacity,
            "vehicle_class": self.vehicle_class
        }