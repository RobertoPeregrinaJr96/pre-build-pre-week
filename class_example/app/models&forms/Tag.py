from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import (IntegerField, StringField, TextAreaField,
                     SubmitField, SelectField, BooleanField)
from wtforms.validators import DataRequired, Length, URL

db = SQLAlchemy()


colors = ["white", "black", "green", "blue",
          "red", "orange", "green", "yellow", "cyan"]


class Tags(db.Model):
    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    # color = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.datetime.utcnow)

    notes = db.relationship("NoteTags", secondary="tags", back_populates="tag")


def check_name(form, field):
    uniqueUsername = Tags.query.filter(Tags.data["username"]).all
    if field.data["name"] == uniqueUsername:
        raise ValidationError("tag with this name already exist")


class TagForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Check_Name()])
    # color = SelectField(
    #     "Color", choices=[i for i in colors], validators=[DataRequired()])
