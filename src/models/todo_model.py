from . import db
class Todo(db.Model):
    __tablename__ = 'todos'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    completed = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime)