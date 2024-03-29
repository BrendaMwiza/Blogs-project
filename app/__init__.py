from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask import Flask
from config import config_options
from flask import Blueprint
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail

bootstrap = Bootstrap()
db = SQLAlchemy()

photos = UploadSet('photos',IMAGES)
mail = Mail()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def kora_app(config_name):
    app = Flask(__name__)

    #Creating app configurations
    app.config.from_object(config_options[config_name])

    #Initializing flask extension
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    #Registering the Blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    # setting config
    from .requests import configure_request
    configure_request(app)

    # configure UploadSet
    configure_uploads(app,photos)

    return app