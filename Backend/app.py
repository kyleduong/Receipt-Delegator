from flask import Flask, jsonify, request, url_for, redirect, render_template, flash
from flask_cors import CORS, cross_origin
import requests, json, re
from flask_sqlalchemy import SQLAlchemy
from models import db, People
import atexit
from foodFinderML import find_food_items

app = Flask(__name__)

app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

CORS(app)

db.init_app(app)

# Define a route to fetch data
@app.route('/', methods=['GET', 'POST'])
def get_data(worked=None):
    if request.method == "POST":
        user = request.form["searchBox"]
        return redirect(url_for("user", usr = user))
    else:
        return render_template("index.html")


# CORS issue fixed because I added more fields to People()?
@app.route('/addPerson', methods=['POST'])
def addPerson():
    namePerson = request.json.get("name")
    if not namePerson:
        return jsonify({"message": "No name provided"}), 400
    
    person = People.query.filter_by(name=namePerson).first()
    if person is None:
        new_price = People(
            name = namePerson,
            ordered = [],
            owed = 0.0
        )
        db.session.add(new_price)
        db.session.commit()
        return jsonify({"message": "Person added successfully to DB"}), 201
    else:
        return jsonify({"message": "Person already exists."}), 200

# reads all of the database objects
@app.route('/people', methods=['GET'])
def get_all_people():
    prices = People.query.all()
    return jsonify([{
        'id': price.id,
        'name': price.name,
        'ordered': price.ordered,
        'owed' : price.owed,
    } for price in prices])
    
# runs the receipt scanner
@app.route('/getFoods')
def getFoods():
    with app.app_context():
        return find_food_items()

# will update the Ordered Parameter and also get the owed amount and add it to previously standing owed
# CORS issue fixed when i removed the [] brackets from the extractPrice function.
# ex: total_price = sum([prices]) -> total_price = sum(prices)
@app.route('/updateOrdered', methods=['PUT'])
def update_ordered():
    data = request.json
    if not data:
        return jsonify({"message": "No data provided"}), 400
    
    for name, items in data.items():
        person = People.query.filter_by(name=name).first()
        if person:
            person.ordered = json.dumps(items)

            # Extract prices from the new ordered items
            prices = extractPrice(json.dumps(items))
            # Ensure owed is a valid number
            if person.owed is None:
                person.owed = 0.0
            
            # Update the owed amount
            person.owed += prices
            db.session.commit()
    
    return jsonify({"message": "Ordered items and Amount owed updated successfully"}), 200

@app.route('/updateOwed', methods=['PUT'])
def update_owed():
    data = request.json
    if not data:
        return jsonify({"message": "No data provided"}), 400
    
    for name, items in data.items():
        person = People.query.filter_by(name=name).first()
        if person:
            prices = extractPrice(json.dumps(items))
            person.owed = person.owed + prices
            db.session.commit()
    
    return jsonify({"message": "Ordered items updated successfully"}), 200

# returns the ordered text of the person with given name
@app.route('/getOrdered', methods=['GET'])
def get_ordered(name):
    name = request.args.get('name')
    if not name:
        return jsonify({"message": "Name parameter is required"}), 400
        
    person = People.query.filter_by(name=name).first()
    if not person:
        return jsonify({"message": "Person not found"}), 404
    
    return person.get_ordered(), 200



@app.route('/getOwed', methods=['GET'])
def get_owed():
    namePerson = request.args.get('name')
    if not namePerson:
        return jsonify({"message": "No name provided"}), 400
    
    person = People.query.filter_by(name=namePerson).first()
    if not person:
        return jsonify({"message": "Person not found"}), 404
    
    return jsonify({
            'owed' : person.owed,
        })

def extractPrice(text):
    # Regular expression pattern to find prices
    pattern = r'\b\d+\.\d{2}\b'
    
    # Find all occurrences of the pattern
    prices = re.findall(pattern, text)
    
    # Convert the found prices to float and return
    prices = [float(price) for price in prices]

    # Calculate total price
    total_price = sum(prices)

    return total_price


if __name__ == '__main__':
    # Initialize the database
    with app.app_context():
        db.create_all()
    app.run(debug=True)