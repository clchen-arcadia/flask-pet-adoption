from random import choices
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, AnyOf


class AddPetForm(FlaskForm):
    """
        Form for adding a new pet for adoption.
    """

    name = StringField("Pet Name", validators=[InputRequired()])
    species = StringField("Species", validators=[
        InputRequired(),
        AnyOf(['dog','cat','porcupine'], "Hey that's not a valid pet")
    ])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = SelectField("Age",
                      choices=[
                          ('baby', 'Baby'),
                          ('young', 'Young'),
                          ('adult', 'Adult'),
                          ('senior', 'Senior')
                      ])
    notes = StringField("Notes")

class EditPetForm(FlaskForm):
    """
        Form to edit a given pets' info.
    """

    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    notes = StringField("Notes")
    available = BooleanField("Available?")