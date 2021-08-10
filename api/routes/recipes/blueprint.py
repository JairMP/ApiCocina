from flask import request, Blueprint
from flask_restful import Api
from api.routes.recipes.add_recipe import Add_Recipe

recipes_bp = Blueprint('recipes', __name__, url_prefix="/recipes")
api = Api(recipes_bp)
api.add_resource(Add_Recipe, '/add')
