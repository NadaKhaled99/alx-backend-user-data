#!/usr/bin/env python3
"""
Implement a hash_password function that 
Expects one string argument
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """ Implement a hash_password function that 
	expects one string argument  """
    encoded = password.encode()
    hashed = bcrypt.hashpw(encoded, bcrypt.gensalt())

    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Implement a hash_password function that 
        expects one string argument  """
    valid = False
    encoded = password.encode()
    if bcrypt.checkpw(encoded, hashed_password):
        valid = True
    return valid
