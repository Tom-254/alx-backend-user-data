#!/usr/bin/env python3
"""Module to manage the API authentication.
"""
import re
from typing import List, TypeVar
from flask import request


class Auth:
    """Class to manage the API authentication.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks if a path requires authentication.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """Returns authorization header.
        """

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns current user.
        """
        return None
