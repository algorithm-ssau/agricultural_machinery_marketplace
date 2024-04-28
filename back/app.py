"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""
# -*- coding: utf-8 -*-
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
#from app import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Waterandwater63@localhost/backend'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
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

    def __repr__(self):
        return f'Type technic {self.type_technic}>'

class User(db.Model):
    idUser = db.Column(db.Integer, primary_key = True)
    login = db.Column(db.String(30), unique = True, nullable = False)
    password = db.Column(db.String(30), unique = True, nullable = False)

    def __repr__(self):
        return f'User {self.login}>'

class Order(db.Model):
    idOrder = db.Column(db.Integer, primary_key = True)

    idTechnic = db.Column(db.Integer, db.ForeignKey('technic.idTechnic'), nullable = False)

    idUser = db.Column(db.Integer, db.ForeignKey('user.idUser'), nullable = False)

    def __repr__(self):
        return f'Number order {self.idOrder}>'

app.app_context().push()
db.create_all()

@app.route('/')
def index():
    return render_template("C:\Users\mande\source\repos\web_project\static\templates\WebPage1.html")

@app.route('/adm_login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        return render_template('login_adm.html')
if __name__ == '__main__':
    app.run(debug = True)

