from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'some$3cretKey'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://ubuntu:password@localhost/users"
app.config['UPLOAD_FOLDER']= "./app/static/photos"
db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views, models