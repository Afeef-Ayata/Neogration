from dotenv import dotenv_values
from mongoengine import connect
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

# init cloud MongoDb
config = dotenv_values(".env")
connect(host=config["ATLAS_URI"])

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def login_user(user_id):
        # since the user_id is just the primary key for our user table, us it in the query for the user
        return User.objects(pk=user_id).first()


    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # register blueprint for editor parts of app
    from .editor import editor as editor_blueprint
    app.register_blueprint(editor_blueprint)

    return app