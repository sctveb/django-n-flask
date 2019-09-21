from flask_sqlalchemy import SQLAlchemy
import datetime
db = SQLAlchemy()

class Todo(db.Model):
    __tablename__ = "todos"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.Text)
    deadline = db.Column(db.DateTime)
    
    def __init__(self,title,content,deadline):
        self.title = title
        self.content = content
        self.deadline = deadline
        