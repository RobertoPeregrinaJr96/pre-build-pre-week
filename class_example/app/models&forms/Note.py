from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import (IntegerField, StringField, TextAreaField,
                     SubmitField, SelectField, BooleanField, DateField)
from wtforms.validators import DataRequired, Length, Email

db = SQLAlchemy()


class Notes(db.Model):
    __tablename__ = "notes"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    body = db.Column(db.StringField)
    trash = db.Column(db.Boolean)
    ownerId = db.Column(db.Integer, db.ForeignKey("Users.id"))
    notebookId = db.Column(db.Integer, db.ForeignKey("Notebooks.id"))
    tagId = db.Column(db.Integer, db.ForeignKey("Tags.id"))
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.datetime.utcnow)

    owner_id = db.relationship(
        "Users", back_populates="Notebooks", cascade="all, delete")
    notebook_id = db.relationship(
        "Notebooks", back_populates="Notebooks", cascade="all, delete")
    tagId = db.relationship(
        "Tags", back_populates="Tags", cascade="all,delete")


class NoteForm(FlaskForm):
    title = StringField("Title")
    body = TextAreaField("Write away")
    trash = BooleanField("Trash?",  false_values=False)
    '''
        Maybe hide these from the JinJa but manually input the data when creating the user
        # created_at = DateField("Created At")
        # updated_at = DateField("Updated At")
    '''
