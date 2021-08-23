"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for, json
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Planet, Character, Vehicle
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def get_user():

    users = User.query.all()
    map_users = [u.serialize() for u in users]
    return jsonify(map_users), 200

@app.route('/planet', methods=['GET'])
def get_planet():

    planets = Planet.query.all()
    map_planets = [u.serialize() for u in planets]
    return jsonify(map_planets), 200

@app.route('/character', methods=['GET'])
def get_char():

    chars = Character.query.all()
    map_chars = [u.serialize() for u in chars]
    return jsonify(map_chars), 200

@app.route('/vehicle', methods=['GET'])
def get_vehicle():

    vehicles = Vehicle.query.all()
    map_vehicles = [u.serialize() for u in vehicles]
    return jsonify(map_vehicles), 200

@app.route('/user', methods=['POST'])
def post_user():
    request_data = request.data
    body = json.loads(request_data)
    user1 = User(username=body['username'], email=body['email'], first_name=body['first_name'], last_name=body['last_name'])
    db.session.add(user1)
    db.session.commit()
    return jsonify(user1.serialize())

@app.route('/planet', methods=['POST'])
def post_planet():
    request_data = request.data
    body = json.loads(request_data)
    planet1 = Planet(name=body['name'], population=body['population'], terrain=body['terrain'], climate=body['climate'], diameter=body['diameter'], gravity=body['gravity'])
    db.session.add(planet1)
    db.session.commit()
    return jsonify(planet1.serialize())

@app.route('/character', methods=['POST'])
def post_character():
    request_data = request.data
    body = json.loads(request_data)
    char1 = Character(name=body['name'], height=body['height'], hair_color=body['hair_color'], eye_color=body['eye_color'], birth_year=body['birth_year'], gender=body['gender'])
    db.session.add(char1)
    db.session.commit()
    return jsonify(char1.serialize())

@app.route('/vehicle', methods=['POST'])
def post_vehicle():
    request_data = request.data
    body = json.loads(request_data)
    vehicle1 = Vehicle(name=body['name'], model=body['model'], manufaturer=body['manufaturer'], cost_in_credits=body['cost_in_credits'], cargo_capacity=body['cargo_capacity'], vehicle_class=body['vehicle_class'])
    db.session.add(vehicle1)
    db.session.commit()
    return jsonify(vehicle1.serialize())


# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)