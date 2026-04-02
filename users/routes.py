from flask import jsonify
from flask_jwt_extended import jwt_required
from app.users import users_bp
from app.models import User
from app.users.schemas import user_to_dict

@users_bp.route('/', methods=['GET'])
@jwt_required()
def get_users():
    users = User.query.all()
    return jsonify([user_to_dict(u) for u in users])
