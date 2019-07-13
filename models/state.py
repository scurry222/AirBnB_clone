#!/usr/bin/python3
""" state.py - 1 class """
from models.base_model import BaseModel


class State(BaseModel):
    """ State class that inherits attributes from base model

        Attributes
        ----------
        name: str
           the name of the state
        state_id: str
           The identification of the state
        all attributes from BaseModel are inherited
    """

    name = ""
    state_id = ""
