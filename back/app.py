"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Waterandwater63@localhost/backend'
db = SQLAlchemy(app)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

class Technic(db.Model):
    idTechnic = db.Column(db.Integer, primary_key = True)
    type_technic = db.Column(db.String(40), unique = False, nullable = False)
    condition = db.Column(db.String(40), unique = False, nullable = False)
    power = db.Column(db.Integer, unique = False, nullable = True)
    working_width = db.Column(db.Integer, unique = False, nullable = False)
    description = db.Column(db.String(120), unique = True, nullable = True)

class User(db.Model):
    idUser = db.Column(db.Integer, primary_key = True)
    login = db.Column(db.String(30), unique = True, nullable = False)
    password = db.Column(db.String(30), unique = True, nullable = False)

class Order(db.Model):
    idOrder = db.Column(db.Integer, primary_key = True)

    idTechnic = db.Column(db.Integer, db.ForeignKey('technic.idTechnic'), nullable = False)
    technic = db.relationship('Technic', backref = db.backref('id', lazy = True))

    idUser = db.Column(db.Integer, db.ForeignKey('user.idUser'), nullable = False)
    user = db.relationship('User', backref = db.backref('number', lazy = True))

app.app_context().push()
db.create_all()


@app.route('/')
def hello():
    """Renders a sample page."""
    return "Hello World!"

if __name__ == '__main__':
    app.run(debug = True)
