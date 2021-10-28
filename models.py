import os
from sqlalchemy import Column, String, Integer, create_engine, TIMESTAMP
from sqlalchemy_utils import database_exists, create_database
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import json

'''
export DB_USER="mongoAdmin"
export DB_PASSWORD="mongoAdmin"
export DB_PORT="27017"
export DB_NAME="webscrap1"
export DB_HOST="127.0.0.1"
'''

scheme = os.getenv('DB_SCHEME', "postgres")
username = os.getenv('DB_USER', "postgres")
password = os.getenv('DB_PASSWORD', "postgres")
port = os.getenv('DB_PORT', 5432)
db_name = os.getenv('DB_NAME', "translatordb2")
host = os.getenv('DB_HOST', 'localhost')

database_url = os.getenv("DATABASE_URL","{}://{}:{}@{}:{}/{}".format(scheme,username,password,host,port,db_name))
print(database_url)

db = SQLAlchemy()

def setup_db(app, database_url=database_url):
    # # Create an engine object.
    # engine = create_engine(database_url, echo=True)

    # # Create database if it does not exist.
    # if not database_exists(engine.url):
    #     create_database(engine.url)
    # engine.dispose()
    app.config["SQLALCHEMY_DATABASE_URI"] = database_url
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    # db.create_all()





class Message(db.Model):  
  __tablename__ = 'msgs'

  id = Column(Integer, primary_key=True, autoincrement=True)
  text = Column(String)
  translatedtext = Column(String)
  moshakkaltext = Column(String)
  sender_id = db.Column(db.Integer, db.ForeignKey('MyUser.id'), nullable=False)
  receiver_id = db.Column(db.Integer, db.ForeignKey('MyUser.id'), nullable=False)
  timedt = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now(), onupdate=db.func.now())
  sender = db.relationship("MyUser", foreign_keys=[sender_id])
  receiver = db.relationship("MyUser", foreign_keys=[receiver_id])

  def __init__(self, text, translatedtext, moshakkaltext):
    self.text = text
    self.translatedtext = translatedtext
    self.moshakkaltext = moshakkaltext

  def insert(self):
    db.session.add(self)
    db.session.commit()
  
  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'text': self.text,
      'translatedtext': self.translatedtext,
      'moshakkaltext': self.moshakkaltext,
      'timedt': self.timedt,
      'sender_id' : self.sender_id,
      'receiver_id' : self.receiver_id
    }

'''
MyUser

'''
class MyUser(db.Model):  
  __tablename__ = 'MyUser'

  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String)
  phone = Column(String)
  email = Column(String)
  language = Column(String)
  country = Column(String)
  password = Column(String)
  gender = Column(String)
  lastactivedatetimedt = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now(), onupdate=db.func.now())

  def __init__(self, name, phone, email, language, country,password,gender):
    self.name = name
    self.phone = phone
    self.email = email
    self.language = language
    self.country = country
    self.password = password
    self.gender = gender
    # self.lastactivedatetimedt = db.func.now()

  def insert(self):

    db.session.add(self)
    db.session.commit()
  
  def update(self):
    self.lastactivedatetimedt = db.func.now()
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()
    
  def format(self):
    return {
      'id': self.id,
      'name': self.name,
      'phone': self.phone,
      'email': self.email,
      'language': self.language,
      'country': self.country,
      'gender': self.gender,
      'lastactivetimedt' : self.lastactivedatetimedt
      }
      
  def format_special(self,dttime_threshold):
    return {
      'id': self.id,
      'name': self.name,
      'phone': self.phone,
      'email': self.email,
      'language': self.language,
      'country': self.country,
      'lastactivetimedt' : self.lastactivedatetimedt,
      'gender': self.gender,
      'isactive' : self.lastactivedatetimedt >= dttime_threshold
    }
