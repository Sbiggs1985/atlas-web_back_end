#!/usr/bin/env python3
"""Function that runs before each request to ensure authentication."""
import sys
import os
from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from api.v1.auth.auth import Auth
from api.v1.auth.basic_auth import BasicAuth
from api.v1.views.index import app_views

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = getenv("AUTH_TYPE")

if auth == "basic_auth":
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
else:
    from api.v1.auth.auth import Auth
    auth = Auth()


@app.errorhandler(401)
def unauthorized(error) -> str:
    """Unauthorized handler"""
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """Forbidden handler"""
    return jsonify({"error": "Forbidden"}), 403


@app.errorhandler(404)
def not_found(error) -> str:
    """404 error handler"""
    return jsonify({"error": "Not found"}), 404


@app.before_request
def before_request_func():
    """Before_request"""
    if auth:
        excluded_paths = [
            '/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/'
        ]
        if not auth.require_auth(request.path, excluded_paths):
            print(f"Path {request.path} does not require authentication.")
            return

        # Check for Authorization header
        auth_header = auth.authorization_header(request)
        if auth_header is None:
            print("Authorization header missing")
            abort(401)

        # Check for authenticated user
        current_user = auth.current_user(request)
        if current_user is None:
            print("Invalid credentials or user not found")
            abort(403)

        print(f"Authenticated user: {current_user.email}")


if __name__ == "__main__":
    """
Runs the Flask app with host and port set from environment variables.
Defaults to '0.0.0.0' and '5000' if environment variables are not set.
"""
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
