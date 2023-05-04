#!/usr/bin/env python3
"""Session authentication that allows session expiration.
"""
import os
from flask import request
from datetime import datetime, timedelta

from .session_auth import SessionAuth


class SessionExpAuth(SessionAuth):
    """Class SessionExpAuth that models session authentication
    with expiration. importing from SessionAuth
    """

    def __init__(self) -> None:
        """Initializes a SessionExpAuth instance.
        """
        super().__init__()
        try:
            self.session_duration = int(os.getenv('SESSION_DURATION', '0'))
        except Exception:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """Creates a Session ID for a user_id
        """
        session_id = super().create_session(user_id)
        if not isinstance(session_id, str):
            return None
        self.user_id_by_session_id[session_id] = {
            'user_id': user_id,
            'created_at': datetime.now(),
        }
        return session_id

    def user_id_for_session_id(self, session_id=None) -> str:
        """Returns a User ID based on a Session ID:
        """

        if session_id in self.user_id_by_session_id:
            session_dict = self.user_id_by_session_id[session_id]
            if self.session_duration <= 0:
                return session_dict['user_id']
            if 'created_at' not in session_dict:
                return None
            current_time = datetime.now()
            time_elapsed = timedelta(seconds=self.session_duration)
            exp_time = session_dict['created_at'] + time_elapsed
            if exp_time < current_time:
                return None
            return session_dict['user_id']
