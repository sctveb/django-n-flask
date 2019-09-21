from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/app')
def app_web():
    return render_template('app.html')
    

@app.route('/signup_01')
def signup_01():
    return render_template('signup_01.html')
    
@app.route('/signup_02')
def signup_02():
    return render_template('signup_02.html')

@app.route('/signup_03')
def signup_03():
    return render_template('signup_03.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/find_password_01')
def find_password_01():
    return render_template('find_password_01.html')

@app.route('/find_password_02')
def find_password_02():
    return render_template('find_password_02.html')