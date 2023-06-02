from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import (IntegerField, StringField, TextAreaField,
                     SubmitField, SelectField, BooleanField, DateField)
from wtforms.validators import DataRequired, Length, Email

db = SQLAlchemy()

"""
-- Notebook --
* able to CREATE
* able to READ
* able to UPDATE
* able to DELETE
----------------------------------------------------------------------------

"""


class Notebooks(db.Model):
    __tablename__ = "notebooks"
    # Table Columns
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(50), nullable=False)
    is_default = db.Column(db.Boolean, nullable=False)
    ownerId = db.Column(db.Integer, db.ForeignKey("User.id"))
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.datetime.utcnow)
    # Relationships
    owner = db.relationship(
        "User", back_populates="User", cascade="all, delete")


"""
* --- Form for Notebook -----


"""


def ChangeDefault():
    current_default = Notebooks.query.filter(Notebooks.is_default == True).all
    current_default = False


class NotebookForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(
        min=1, max=50, message="Your notebook name must contain at least one character")])
    is_default = BooleanField(
        "Set this as your default Notebook?", validators=[DataRequired(), ChangeDefault()])
    '''
        Maybe hide these from the JinJa but manually input the data when creating the user
        # created_at = DateField("Created At")
        # updated_at = DateField("Updated At")
    '''