"""Seed file to make """

from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

#lmao. not my fault
BEAGLE_IMG_URL = 'https://s3.amazonaws.com/cdn-origin-etr.akc.org/wp-content/uploads/2016/06/24151048/Beagle-standing-in-a-frosty-field-on-a-cold-morning.jpg'

# Add users
whiskey = Pet(
    name= 'Whiskey',
    species = 'dog',
    photo_url = BEAGLE_IMG_URL,
    age = 'adult',
)

# Add new users to session
db.session.add(whiskey)

# commit session
db.session.commit()
