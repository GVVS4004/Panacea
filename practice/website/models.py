# # from datetime import datetime
# # from . import crete_app
# from werkzeug.security import generate_password_hash, check_password_hash
# from flask_login import UserMixin
# from uuid import uuid4
# from . import db
# # app=crete_app.create_app()
# # @app.login.user_loader
# # def load_user(id):
# #     return User.objects.get(id=id)

# from flask import Flask,jsonify

# class User(UserMixin):
#     def new_user(firstname,lastname,password,email,phno):
#         id=uuid4().hex
#         user={
#             '_id':id,
#             'fristname':firstname,
#             'lastname':lastname,
#             'email':email,
#             'password':password,
#             'mobile':phno,
#             'is_active':True,
#             'get_id':id,
#             'is_authenticated':True,
#             'is_anonymous':False
#             }
#         return user
import datetime
import uuid
from flask import session, flash
from flask_login import login_manager
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

class User(UserMixin):

    def __init__(self, firstname,lastname, email, password,phno,_id=None):
        self.firstname= firstname
        self.lastname=lastname
        self.email = email
        self.password = password
        self.phno=phno
        self._id = uuid.uuid4().hex if _id is None else _id

    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return self._id

    @classmethod
    def get_by_username(cls, firstname):
        data = db.db.user.find_one({"firstname": firstname})
        if data is not None:
            
            return cls(**data)

    @classmethod
    def get_by_email(cls,email):
        data = db.db.user.find_one({"email": email})
        # print(data)
        if data is not None:
            # print(cls(data))
            return cls(**data)

    @classmethod
    def get_by_id(cls, _id):
        data = db.db.user.find_one({"_id": _id})
        if data is not None:
            return cls(**data)

    @staticmethod
    def login_valid(email, password):
        verify_user = User.get_by_email(email)
        if verify_user is not None:
            return check_password_hash(verify_user.password, password)
        return False

    @classmethod
    def register(cls, firstname,lastname, email, password,phno):
        user = cls.get_by_email(email)
        if user is None:
            new_user = cls( firstname,lastname, email, password,phno)
            new_user.save_to_mongo()
            session['email'] = email
            return True
        else:
            return False

    def json(self):
        return {
            "_id": self._id,
            "firstname": self.firstname,
            'lastname':self.lastname,
            "email": self.email,
            'phno':self.phno,
            "password": self.password
        }
    def save_to_mongo(self):
        db.db.user.insert_one( self.json())