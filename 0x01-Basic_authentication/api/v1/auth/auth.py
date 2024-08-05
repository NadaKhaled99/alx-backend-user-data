#!/usr/bin/env python3
""" Create a class to manage the API authentication
"""
from flask import request
from typing import List, TypeVar
import fnmatch


class Auth:
    """ Create a class to manage the API authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Create a class to manage the API authentication
        """
        if path is None:
            return True

        if excluded_paths is None or not excluded_paths:
            return True

        for excluded_path in excluded_paths:
            if fnmatch.fnmatch(path, excluded_path):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Create a class to manage the API authentication
        """
        if request is not None:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Create a class to manage the API authentication
        """
        return None
