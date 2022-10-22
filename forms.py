from flask_wtf import FlaskForm
# Ask: what is good practice for cleaning up from import lines?
from wtforms import (
    StringField,
    FloatField, #TODO usually remove this!
    SelectField,
    BooleanField,
    TextAreaField
)#TODO like this!
from wtforms.validators import InputRequired, Optional, URL, AnyOf

#AVAILABLE_CHOICES = [( , ), ( , )]


class AddPetForm(FlaskForm):
    """
        Form for adding a new pet for adoption.
    """

    name = StringField("Pet Name", validators=[InputRequired()])
    species = StringField(
        "Species",
        validators=[
            InputRequired(),
            AnyOf(['dog','cat','porcupine'], "Hey that's not a valid pet")
        ]
    ) #TODO select field for this is advisable
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = SelectField("Age",
                      choices=[
                          ('baby', 'Baby'),
                          ('young', 'Young'),
                          ('adult', 'Adult'),
                          ('senior', 'Senior')
                      ])
    notes = TextAreaField("Notes")#TODO add validators optional. but WTForm behavior has changed??

class EditPetForm(FlaskForm):
    """
        Form to edit a given pets' info.
    """

    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    notes = TextAreaField("Notes")
    available = BooleanField("Available?")
