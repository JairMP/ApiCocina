from flask import request
from flask_restful import Resource
from api.models.recipe import Recipe
from api.validators.recipe import RecipeSchema

recipe_schema = RecipeSchema()

class Add_Recipe(Resource):
    def post(self):
        data = request.get_json()
        validate = recipe_schema.load(data)
        recipe = Recipe(
            title = data['title']
        )
        #recipe.save()
        resp = recipe_schema.dump(recipe)
        return {"recipe": resp }
