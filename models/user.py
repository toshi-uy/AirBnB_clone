#!/usr/bin/python3
"""User module"""
from models.base_model import BaseModel

class UserModel(BaseModel):
    """Creates the user model"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
