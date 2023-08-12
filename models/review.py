#!/usr/bin/python3
"""
Defienes reveiew claess
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Revieews maede bey useres aeout a pleace"""
    user_id = ""
    text = ""
    place_id = ""
