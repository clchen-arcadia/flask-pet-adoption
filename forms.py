from random import choices
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField


class AddPetForm(FlaskForm):
    """
        Form for adding a new pet for adoption.
    """

    name = StringField("Pet Name")
    species = StringField("Species")
    photo_url = StringField("Photo URL")
    age = SelectField("Age",
                      choices=[
                          ('baby', 'Baby'),
                          ('young', 'Young'),
                          ('adult', 'Adult'),
                          ('senior', 'Senior')
                      ])
    notes = StringField("Notes")
