from flask import jsonify

def success(data):
    return jsonify(data), 200

def error(message, code=400):
    return jsonify({"error": message}), code
