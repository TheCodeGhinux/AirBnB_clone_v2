#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import Base, BaseModel


class Review(BaseModel, Base):
    """ Review class to store review information

    Inherits from SQLAlchemy Base and links to the MySQL table reviews.

    Attributes:
        __tablename__ (str): Name of the Sql table.
        text (sqlalchemy String): Description of review.
        place_id (sqlalchemy String): Review Id.
        user_id (sqlalchemy String): User id of reviewer.
    """
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
