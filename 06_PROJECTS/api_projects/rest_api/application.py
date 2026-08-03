"""
An exercise on API creation
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Setup your flask
app = Flask(__name__)

# Create the database for Sqlalchemy
# We need to connect to a database and define our items as models
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} - {self.description}"



# Make an endpoint
@app.route('/')
def index():
    return 'Hello'

# Make Get request to make our app store drinks
@app.route('/drinks')
def get_drinks():
    return {
        "drinks": ["nutrimilk", "cocacola", "7up"]
        }

# if __name__ == "__main__":
#     with app.app_context():
#         db.create_all()