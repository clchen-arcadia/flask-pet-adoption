"""Seed file to make """

from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

#lmao. not my fault
BEAGLE_IMG_URL = 'https://m.media-amazon.com/images/I/91NZxCEYzvL._CR0,412,1060,1060_UX256.jpg'
PORCUPINE_IMG_URL = 'https://styles.redditmedia.com/t5_as0re/styles/profileIcon_5mlz3641bpb01.jpg?width=256&height=256&frame=1&crop=256:256,smart&s=89ee058b6330f166c5dbba2275758cefe972b082'

# Add users
whiskey = Pet(
    name= 'Whiskey',
    species = 'dog',
    photo_url = BEAGLE_IMG_URL,
    age = 'adult',
    notes = "He's a very good boy!!! <3"
)

michael = Pet(
    name='Michael',
    species = 'porcupine',
    photo_url = PORCUPINE_IMG_URL,
    age = 'baby',
    available = False
)


# Add new users to session
db.session.add(whiskey)
db.session.add(michael)

# commit session
db.session.commit()
