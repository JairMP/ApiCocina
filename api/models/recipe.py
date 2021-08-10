from api.db import db, BaseModel


class Recipe(db.Model, BaseModel):
    __tablename__ = 'recipes'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)

    def __repr__(self):
        return f'Film({self.title})'
