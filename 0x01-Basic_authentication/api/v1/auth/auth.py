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
        if path is not None and excluded_paths is not None:
            for excluded_path in excluded_paths:
                excluded_regex = '^{}$'.format(re.escape(
                    excluded_path.rstrip('/')).replace('\\*', '.*') + '/?.*')
                if re.match(excluded_regex, path):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """Returns authorization header.
        """

        return request.headers.get('Authorization') if request else None

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns current user.
        """
        return None
