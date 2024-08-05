#!/usr/bin/env python3
""" Add a new endpoint in api/v1/views/index.py
"""
from flask import jsonify, abort
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ Add a new endpoint in api/v1/views/index.py
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats/', strict_slashes=False)
def stats() -> str:
    """ Add a new endpoint in api/v1/views/index.py
    """
    from models.user import User
    stats = {}
    stats['users'] = User.count()
    return jsonify(stats)


@app_views.route('/unauthorized/', strict_slashes=False)
def unauthorized() -> None:
    """Add a new endpoint in api/v1/views/index.py
    """
    abort(401)


@app_views.route('/forbidden/', strict_slashes=False)
def forbidden() -> None:
    """Add a new endpoint in api/v1/views/index.py
    """
    abort(403)
