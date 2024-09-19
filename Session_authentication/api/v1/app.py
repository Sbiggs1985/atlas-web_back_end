#!/usr/bin/env python3
"""This module defines a simple Flask application"""
import sys
import os
from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from api.v1.auth.auth import Auth
from api.v1.auth.basic_auth import BasicAuth
from api.v1.auth.session_auth import SessionAuth
from api.v1.views.index import app_views

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '../../..')
    )
)

app = Flask(__name__)
CORS(app)

app.register_blueprint(app_views)

auth = None
AUTH_TYPE = os.getenv('AUTH_TYPE')

if AUTH_TYPE == 'basic_auth':
    auth = BasicAuth()
elif AUTH_TYPE == 'session_auth':
    auth = SessionAuth()
else:
    auth = Auth()


@app.errorhandler(401)
def unauthorized(error):
    """Handles 401 Unauthorized errors."""
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error):
    """Handles 403 Forbidden errors."""
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def before_request_func():
    """Function that runs before each request"""
    if auth:
        excluded_paths = [
            '/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/',
            '/api/v1/auth_session/login/'
        ]
        if not auth.require_auth(request.path, excluded_paths):
            print(f"Path {request.path} does not require authentication.")
            return

        if AUTH_TYPE == 'basic_auth':
            if auth.authorization_header(request) is None:
                print("Authorization header missing")
                abort(401)

        if AUTH_TYPE == 'session_auth':
            if auth.session_cookie(request) is None:
                print("Session cookie missing")
                abort(401)

        request.current_user = auth.current_user(request)
        if request.current_user is None:
            print("Invalid credentials or user not found")
            abort(403)

        print(f"Authenticated user: {request.current_user.email}")


if __name__ == "__main__":
    host = os.getenv("API_HOST", "0.0.0.0")
    port = os.getenv("API_PORT", "5000")
    app.run(host=host, port=port)
