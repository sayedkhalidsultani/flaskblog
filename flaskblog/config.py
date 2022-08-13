import os 
import creds

class Config:
    SECRET_KEY = creds.SECRET_KEY
    SQLALCHEMY_DATABASE_URI = creds.SQLALCHEMY_DATABASE_URI