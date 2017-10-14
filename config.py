from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_HOST'] = "ds119395.mlab.com"
app.config['MONGO_PORT'] = 19395
app.config['MONGO_DBNAME'] = "crimedata"
app.config['MONGO_USERNAME'] = "**********"
app.config['MONGO_PASSWORD'] = "**********"

mongo = PyMongo(app)
