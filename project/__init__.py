from mongoengine import connect
from flask import Flask
from flask_login import LoginManager
from os import environ

# init cloud MongoDb
connect(host=environ.get("ATLAS_URI"))

def create_app():
    app = Flask(__name__)

    # set the secret_key
    # this is need to maintain user sessions
    app.config['SECRET_KEY'] = 'secret-key-goes-here'

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def login_user(user_id):
        # since the user_id is just the primary key for our user table, use it in the query for the  user
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

    from .editor import my_neoworks, my_neoscripts, getScriptById
    app.jinja_env.globals.update(getMyWorks=my_neoworks)
    app.jinja_env.globals.update(getMyScripts=my_neoscripts)
    app.jinja_env.globals.update(getScriptById=getScriptById)

    from .job import job as job_blueprint
    app.register_blueprint(job_blueprint)
    

    return app