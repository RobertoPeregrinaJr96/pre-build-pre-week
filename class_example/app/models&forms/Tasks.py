from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import (IntegerField, StringField, TextAreaField,
                     SubmitField, SelectField, BooleanField, DateField)
from wtforms.validators import DataRequired, Length, Email

db = SQLAlchemy()


class Tasks(db.Model):
    __tablename__ = "tasks"
    # Table Columns
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    ownerId
    description = db.Column(db.String)
    completed = db.Column(db.Boolean, default=False)
    due_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.datetime.utcnow)
    # relationships
    owner = db.relationship(
        "Users", back_populates="User", cascade="all,delete")


class TaskForm(FlaskForm):
    title = StringField("Name of Task", validators=[
                        DataRequired(), Length(min=5, max=50)])
    description = TextAreaField(
        "Description of said task", validators=[DataRequired()])
    completed = BooleanField("Completed?", default=False)
    due_date = DateField("when should this task be completed?",)
    '''
        Maybe hide these from the JinJa but manually input the data when creating the user
        # created_at = DateField("Created At")
        # updated_at = DateField("Updated At")
    '''
