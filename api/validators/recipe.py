from marshmallow import fields
from api.ext import ma

class RecipeSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String()
    