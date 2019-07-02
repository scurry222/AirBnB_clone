#!/usr/bin/python3
""" state.py - 1 class """
from models.base_model import BaseModel


class State(BaseModel):
    """ State class that inherits attributes from base model
    Args:
        BaseModel('class'): include attributes
    """

    name = ""
    state_id = ""
