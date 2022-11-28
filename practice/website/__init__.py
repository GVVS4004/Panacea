from flask import Flask
from flask_login import LoginManager
from flask_pymongo import PyMongo
from os import path
from .extensions import db
from pymongo import MongoClient

class crete_app():
    def create_app():
        app=Flask(__name__)
        app.config['SECRET_KEY']='ivnfidoivndfvindvfosjfv'
        app.config['MONGO_URI']='mongodb://localhost:27017/Users'
        app.config['UPLOAD_FOLDER']='static/image_uploads'
        db.init_app(app)
        

        from .views import views
        from .auth import auth
        app.register_blueprint(views,url_prefix="/")
        app.register_blueprint(auth,url_prefix="/")
        from .models import User
        login_manager=LoginManager()
        login_manager.login_view='auth.login'
        login_manager.init_app(app)
        @login_manager.user_loader
        def load_user(user_id):
            user =User.get_by_id(user_id)
            # print(user,"****")
            if user is not None:
                return User(user.firstname,user.lastname,user.email,user.password,user.phno,user._id)
            else:
                return None

        
        return app
        


