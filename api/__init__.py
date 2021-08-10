import os
from flask import Flask
from api.db import db
from flask_restful import Api
from api.ext import ma
from api.routes.recipes.blueprint import recipes_bp

def create_app(settings_module, name):
    
    app = Flask(name)
    app.config.from_object(settings_module)

    db.init_app(app)
    ma.init_app(app)

    Api(app)

    app.register_blueprint(recipes_bp)
    
    return app