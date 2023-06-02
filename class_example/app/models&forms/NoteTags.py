from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import (IntegerField, StringField, TextAreaField,
                     SubmitField, SelectField, BooleanField, DateField)
from wtforms.validators import DataRequired, Length, Email

db = SQLAlchemy()


class NoteTags(db.Model):
    __name__ = "note_tags"
    # Table Columns
    id = db.Column(db.Integer, primary_key=True)
    noteId = db.Column(db.Integer, db.ForeignKey(
        add_prefix_for_prod("Notes")), nullable=False)
    tagId = db.Column(db.Integer, db.ForeignKey(
        add_prefix_for_prod("Tags")), nullable=False)
    # relationship
    note = db.relationship("Notes", back_populates="Notes")
    tag = db.relationship("Tags", back_populates="Tags", cascade="all,delete")


# No form since this is a join table to connect tags to notes as notes can have many tags and tags can be associated to many notes
