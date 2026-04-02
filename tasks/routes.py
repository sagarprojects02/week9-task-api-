from flask import request, jsonify
from flask_jwt_extended import jwt_required
from app.tasks import tasks_bp
from app.models import Task
from app.extensions import db
from app.tasks.schemas import task_to_dict

@tasks_bp.route('/', methods=['GET'])
@jwt_required()
def get_tasks():
    tasks = Task.query.all()
    return jsonify([task_to_dict(t) for t in tasks])

@tasks_bp.route('/', methods=['POST'])
@jwt_required()
def create_task():
    data = request.json
    task = Task(title=data['title'], status=data.get('status', 'pending'))
    db.session.add(task)
    db.session.commit()
    return jsonify(task_to_dict(task)), 201
