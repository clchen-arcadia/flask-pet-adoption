from flask_wtf import FlaskForm
#TODO: Ask: what is good practice for cleaning up from import lines?
from wtforms import StringField, FloatField, SelectField, BooleanField, TextAreaField
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
    notes = TextAreaField("Notes")

class EditPetForm(FlaskForm):
    """
        Form to edit a given pets' info.
    """

    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    notes = TextAreaField("Notes")
    available = BooleanField("Available?")
