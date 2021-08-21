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
    user1 = User(username="my_super_usernasssme0", email="my_super87@email.com", first_name="gabriel", last_name="hernandez")
    db.session.add(user1)
    db.session.commit()
    return jsonify(user1.serialize())
    # user1 = Person.query.get(person_id)
    # if user1 is None:
    #     raise APIException('User not found', status_code=404)

    # if "username" in body:
    #     user1.username = body["username"]
    # if "email" in body:
    #     user1.email = body["email"]
    # db.session.commit()

@app.route('/planet', methods=['POST'])
def post_planet():
    request_data = request.data
    body = json.loads(request_data)
    planet1 = Planet(name=body['name'], population=body['population'], terrain=body['terrain'], climate=body['climate'], diameter=body['diameter'], gravity=body['gravity'])
    db.session.add(planet1)
    db.session.commit()
    return jsonify(planet1.serialize())
    # new_name = request.form['name']
    # name = Clients(name=new_name)
    # session.add(name)
    # session.commit()
    # request_data = request.data
    # print(request_data)
    # # body = json.loads(request_data)
    # planet = request_data['name']
    # db.session.add(planet)
    # db.session.commit()
    # return jsonify(planet.serialize())

    # user1 = Person(username=body['username'], email=body['email'])


@app.route('/character', methods=['POST'])
def post_character():
    char1 = Character(name="Luke Skywalker", height="172", hair_color="Blond", eye_color="Blue", birth_year="19BBY", gender="male")
    db.session.add(char1)
    db.session.commit()
    return jsonify(char1.serialize())

@app.route('/vehicle', methods=['POST'])
def post_vehicle():
    vehicle1 = Vehicle(name="Sand Crawler", model="Digger Crawler", manufaturer="Corellia Mining Corporation", cost_in_credits=150000, cargo_capacity=50000, vehicle_class="wheeled")
    db.session.add(vehicle1)
    db.session.commit()
    return jsonify(vehicle1.serialize())


# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)