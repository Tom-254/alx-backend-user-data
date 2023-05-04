#!/usr/bin/env python3
"""Flask view module that handles all routes
for the Session authentication
"""
import os
from typing import Tuple
from flask import abort, jsonify, request

from models.user import User
from api.v1.views import app_views
from api.v1.app import auth


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> Tuple[str, int]:
    """POST /api/v1/auth_session/login
    Return:
      - JSON representation of a User object.
    """
    error_not_found = {"error": "no user found for this email"}
    email = request.form.get('email')
    if not email or not email.strip():
        return jsonify({"error": "email missing"}), 400
    password = request.form.get('password')
    if not password or not password.strip():
        return jsonify({"error": "password missing"}), 400
    try:
        users = User.search({'email': email})
    except Exception:
        return jsonify(error_not_found), 404
    if len(users) <= 0:
        return jsonify(error_not_found), 404
    if users[0].is_valid_password(password):

        return jsonify(users[0].to_json()).set_cookie(
            os.getenv("SESSION_NAME"),
            auth.create_session(getattr(users[0], 'id')))
    return jsonify({"error": "wrong password"}), 401
