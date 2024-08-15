from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import json

db = SQLAlchemy()

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    ordered = db.Column(db.Text, default="")
    owed = db.Column(db.Float, default=0.0)

    def __init__(self, name, ordered=None, owed=0.0):
        self.name = name
        self.ordered = json.dumps(ordered)
        self.owed = owed

    def get_ordered(self):
        return json.loads(self.ordered)
        
""" # Creating a new record
ordered_list = ["item1", "item2", "item3"]
new_record = PriceHistory(ticker="AAPL", price="150", ordered=ordered_list)
db.session.add(new_record)
db.session.commit()

# Retrieving and deserializing the list
record = PriceHistory.query.first()
print(record.get_ordered())  # Output: ["item1", "item2", "item3"] """