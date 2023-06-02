from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import (IntegerField, StringField, TextAreaField,
                     SubmitField, SelectField, BooleanField, DateField)
from wtforms.validators import DataRequired, Length, Email

db = SQLAlchemy()


"""
-- Users table --
* able to CREATE a new user
* able to READ the users information
* able to UPDATE the current users information
* able to DELETE the current user and all of its information


* -- When CREATING a new user --
    * MUST have a firstName(cannot exceed 50 characters,cannot be empty)
    * MUST have a lastName(cannot exceed 50 characters,cannot be empty)
    * MUST have a email(email must be valid, cannot be empty, must be unique)
    * MUST have a username(cannot exceed 20 characters, cannot be empty, must be unique)

* -- When READING the users info information --
    * have a navigation element(to edit user(modal),to delete user(modal))
    * Extra: able to look up another user by their username/email

* -- When Updating the users information --
    * MUST be Logged in
    * All input fields MUST be filled
    * MUST confirm the changes before submitting
    * Users info will auto populate onto the form upon render

* -- When Deleting the user
    * Must be logged in
    * Must confirm the before deleting everything
    * When the user is deleted it will also delete all relevant relationships(notebook,notes)

------------------------------------------------------------------------------
* User : How the client is able to navigate and save information they put in the server and be protected by credentials

"""


class Users(db.Model):
    __tablename__ = "users"
    # Table Columns
    id = db.Column(db.Integer, primary_key=True)
    # firstName = db.Column(db.String(50), nullable=False)
    # lastName = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.datetime.utcnow)

    tasks = db.relationship("Tasks", back_populates="owner")
    notebooks = db.relationship("Notebooks", back_populates="owner")


"""
* --- Form ---

    * Validations
        - DataRequired(): Checks the field`s data is `truthy` otherwise stops the validation chain.
        - Length(): (min=- 1, max=- 1, message=None)
        - Email(): (i.e. @example.com)

------------------------------------------------------------------------------

* Form for a new User
    1.) the client must fill in the First Name input field
        - the data must be between 1 to 50 characters

    2.) the client must fill in the Last Name input field
        - the data must be between 1 to 50 characters

    3.) the client must fill in the Password input field
        - the data must be between 5 to 20 characters

    4.) the client must fill in the Email input field
        - the data must have "@.email.com" email format
        - the data must be unique

    5.) the client must fill in the Username input field
        - the data must be between 4 to 20 characters
        - the data must be unique
"""

"""
Custom Validators for unique email and username
"""


def check_Email(form, field):
    uniqueEmail = Users.query.filter(User.data["email"]).all()
    if field.data["email"] == uniqueEmail:
        raise ValidationError("account with this email already exist")


def check_Username(form, field):
    uniqueUsername = Users.query.filter(User.data["username"]).all()
    if field.data["username"] == uniqueUsername:
        raise ValidationError("account with this username already exist")


class UserForm(FlaskForm):
    # firstName = StringField("First Name", validators=[
    #                         DataRequired(), Length(min=1, max=50)])
    # lastName = StringField("Last Name", validators=[
    #                        DataRequired(), Length(min=1, max=50)])
    password = IntegerField("Password", validators=[
                            DataRequired(), Length(min=5, max=20)])
    email = StringField("Email", validators=[
                        DataRequired(), Length(min=5, max=50, message="Your email name must be between 5 and 50 characters"), Email(), check_Email()])
    username = StringField("Username", validators=[
                           DataRequired(), Length(min=4, max=20), check_Username()])
    '''
        Maybe hide these from the JinJa but manually input the data when creating the user
        # created_at = DateField("Created At")
        # updated_at = DateField("Updated At")
    '''
