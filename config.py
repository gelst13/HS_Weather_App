import os

key = os.urandom(24)  # specify the length in brackets
SECRET_KEY = key
DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///weather.db'
