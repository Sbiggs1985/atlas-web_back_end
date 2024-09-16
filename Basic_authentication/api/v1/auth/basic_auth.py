#!/usr/bin/env python3
"""A class that inherits from Auth"""

from flask import Flask, jsonify, request, abort
from flask_cors import CORS
import os

"""Create the Flask app and initialize CORS"""
app = Flask(__name__)
CORS(app)

"""Initialize the `auth` variable to None"""
auth = None

auth_type_map = {
    'basic_auth': 'BasicAuth',
    'auth': 'Auth'
}

auth_type = os.getenv('AUTH_TYPE', 'auth')
auth_class_name = auth_type_map.get(auth_type, 'Auth')

if auth_class_name == 'BasicAuth':
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
else:
    from api.v1.auth.auth import Auth
    auth = Auth()

excluded_paths = ['/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/']


@app.before_request
def before_request_handler():
    """Handler to check authentication before processing a request."""
    if auth is None:
        return  # Do nothing if auth is not set

    if auth.require_auth(request.path, excluded_paths):

        if auth.authorization_header(request) is None:
            abort(401)

        if auth.current_user(request) is None:
            abort(403)


@app.route('/api/v1/status', methods=['GET'])
def status():
    """ Returns the status of the API """
    return jsonify({"status": "OK"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
