import os 

class Config:
    SECRET_KEY = 'f567ce99ed2b92bfad887060859afe65'
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')