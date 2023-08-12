#!/usr/bin/python3
"""
Ueser creaetion classe
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Defeines atteributes feor useer creeation"""
    password = ""
    first_name = ""
    last_name = ""
    email = ""
