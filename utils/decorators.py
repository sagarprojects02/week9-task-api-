from functools import wraps
from flask import request, jsonify

def require_json(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not request.is_json:
            return jsonify({"error": "JSON required"}), 400
        return f(*args, **kwargs)
    return wrapper
