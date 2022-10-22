"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """
    Connect this database to provided Flask app.
    You should call this in your Flask app.
    """

    app.app_context().push()
    db.app = app
    db.init_app(app)

    #ALLOWED_SPECIES = '(
    #
    # )'

    #f"species IN {ALLOWED_SPECIES}"


class Pet(db.Model):
    """Pet records for adoption agency"""

    __tablename__ = "pets"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    name = db.Column(
        db.String(50),
        nullable=False,
    )
    species = db.Column(
        db.String(50),
        db.CheckConstraint("species IN ('cat','dog','porcupine')"), #make global string?
        nullable=False,
    )
    photo_url = db.Column(
        db.String(500),
        nullable=False,
        default=''
    )
    age = db.Column(
        db.String(20),
        db.CheckConstraint("age IN ('baby','young','adult','senior')"),
        nullable=False,
    )
    notes = db.Column(
        db.String(1000),
        nullable=True
    )#TODO: nullable=False advisable. default=''
    available = db.Column(
        db.Boolean,
        nullable=False,
        default=True
    )
