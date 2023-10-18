from flask import Flask
from config import config

def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    config[config_name].init_app(app)
    
    register_modules(app)


    return app
def register_modules(app):
    from app.apis import apis_bp

    app.register_blueprint(apis_bp) 
    