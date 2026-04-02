from flask import request, jsonify
from app.auth import auth_bp
from app.models import User
from app.extensions import db
from app.auth.utils import generate_token

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    user = User(username=data['username'], password=data['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify({"msg": "User created"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()
    if user and user.password == data['password']:
        return jsonify(access_token=generate_token(user.id))
    return jsonify({"msg": "Invalid credentials"}), 401
