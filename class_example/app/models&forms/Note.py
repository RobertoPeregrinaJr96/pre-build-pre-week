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
    ownerId = db.Column(db.Integer, db.ForeignKey(
        add_prefix_for_prod("Users.id")), nullable=False)
    notebookId = db.Column(db.Integer, db.ForeignKey(
        add_prefix_for_prod("Notebooks.id")), nullable=False)
    tagId = db.Column(db.Integer, db.ForeignKey(
        add_prefix_for_prod("Tags.id")), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.datetime.utcnow)

    # fix these
    owners = db.relationship(
        "Users", back_populates="notes", cascade="all, delete-orphan")
    notebooks = db.relationship(
        "Notebooks", back_populates="notes", cascade="all, delete-orphan")
    tags = db.relationship(
        "Tags", back_populates="notes", secondary="note_tags", cascade="all, delete-orphan")


class NoteForm(FlaskForm):
    title = StringField("Title")
    body = TextAreaField("Write away")
    trash = BooleanField("Trash?",  false_values=False)
    '''
        Maybe hide these from the JinJa but manually input the data when creating the user
        # created_at = DateField("Created At")
        # updated_at = DateField("Updated At")
    '''
# (datetime.datetime(2012,4,1,0,0) - datetime.datetime(1970,1,1)).total_seconds()
