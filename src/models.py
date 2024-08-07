from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), nullable=False, unique=True)
    email = db.Column(db.String(250), nullable=False, unique=True)
    password_hash = db.Column(db.String(250), nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.set_password(password)
        db.session.add(self)
        try: 
            db.session.commit()
        except Exception as error:
            db.session.rollback()
            raise Exception(error.args)
        
    def __repr__(self):
        return '<User %r>' % self.username

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
        }

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(250))

    def __init__(self, name, description=None):
        self.name = name
        self.description = description
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(250))

    def __init__(self, name, description=None):
        self.name = name
        self.description = description
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }

class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=True)
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'), nullable=True)

    user = db.relationship("User", backref="favorites")
    character = db.relationship("Character")
    planet = db.relationship("Planet")

    def __init__(self, user_id, character_id=None, planet_id=None):
        self.user_id = user_id
        self.character_id = character_id
        self.planet_id = planet_id
    
    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id,
            "planet_id": self.planet_id
        }