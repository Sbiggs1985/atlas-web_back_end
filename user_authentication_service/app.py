#!/usr/bin/env python3
"""Flask app for authentication"""

from auth import Auth
from flask import Flask, jsonify, request, abort, redirect

AUTH = Auth()
app = Flask(__name__)


def get_request_data(fields):
    """Helper to extract fields from request form"""
    return {field: request.form.get(field) for field in fields}


@app.route('/', methods=['GET'], strict_slashes=False)
def welcome() -> str:
    """GET / - Welcome message."""
    return jsonify({"message": "Bienvenue"}), 200


@app.route('/users', methods=['POST'], strict_slashes=False)
def create_user() -> str:
    """POST /users - Create a new user."""
    data = get_request_data(['email', 'password'])
    try:
        AUTH.register_user(data['email'],
                           data['password'])
        return jsonify({"email": data['email'],
                        "message": "user created"}), 200
    except Exception:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> str:
    """POST /sessions - Login a user."""
    data = get_request_data(['email', 'password'])
    if AUTH.valid_login(data['email'], data['password']):
        session_id = AUTH.create_session(data['email'])
        response = jsonify({"email": data['email'], "message": "logged in"})
        response.set_cookie('session_id', session_id)
        return response
    abort(401)


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout() -> str:
    """DELETE /sessions - Logout the user."""
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        AUTH.destroy_session(user.id)
        return redirect('/')
    abort(403)


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile() -> str:
    """GET /profile - Get user profile."""
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        return jsonify({"email": user}), 200
    abort(403)


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token() -> str:
    """POST /reset_password - Get password reset token."""
    data = get_request_data(['email'])
    try:
        token = AUTH.get_reset_password_token(data['email'])
        return jsonify({"email": data['email'], "reset_token": token}), 200
    except Exception:
        abort(403)


@app.route('/reset_password', methods=['PUT'], strict_slashes=False)
def update_password() -> str:
    """PUT /reset_password - Update user's password."""
    data = get_request_data(['email', 'reset_token', 'new_password'])
    try:
        AUTH.update_password(data['reset_token'], data['new_password'])
        return jsonify({"email": data['email'],
                        "message": "Password updated"}), 200
    except Exception:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
