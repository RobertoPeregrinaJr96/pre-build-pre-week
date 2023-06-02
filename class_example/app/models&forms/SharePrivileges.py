from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import (IntegerField, StringField, TextAreaField,
                     SubmitField, SelectField, BooleanField, DateField)
from wtforms.validators import DataRequired, Length, Email

db = SQLAlchemy()


class Share_Privileges(db.Model):
    __tablename__ = "share_privileges"
    # Table Columns
    id = db.Column(db.Integer, primary_key=True)
    ownerId = db.Column(db.Integer, db.ForeignKey("Users.id"))
    tagId = db.Column(db.Integer, db.ForeignKey("Tags.id"))
    read_privileges = db.Column(db.Boolean, default=False)
    write_privileges = db.Column(db.Boolean, default=False)
    #  Relationships
    owner = db.relationship(
        "Users", back_populates="Notebooks", cascade="all, delete")
    tag = db.relationship(
        "Tags", back_populates="Tags")

    # Would this need a form or more of a react component that check if a button(where the JiJna will be housed for the read && write permissions and have a modal for it as well) is pressed to share and the credentials are processed in the Js logic?
