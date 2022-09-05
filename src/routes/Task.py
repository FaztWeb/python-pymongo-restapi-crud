from flask import Blueprint, jsonify, request, Response, abort
from bson import json_util
from bson.objectid import ObjectId
from mongodb import mongo
from models.Task import Task as TaskRepo


Task = Blueprint('task', __name__, url_prefix="/task")


@Task.route('/', methods=['POST'])
def create_task():
    data = request.get_json()
    ReferenceTask = TaskRepo.from_dict(data)
    if ReferenceTask:
        result = mongo.db.task.insert_one(ReferenceTask.to_dict())
        ReferenceTask._id = str(result.inserted_id)
        return Response(
            response={"message": f"Task created id: {str(result.inserted_id)}"},
            status = 200,
            mimetype="application/json"
        )
    else:
        abort(404)

@Task.route('/id/addnote', methods=['PUT'])
def add_team_member(id):
    data = request.get_json()
    mongo.db.project.update_one(
        {'_id': ObjectId(id)}, {'$push': {"notes": data}})
    return Response(
        response={'message': 'Project' + id + 'Updated Team Member Successfuly'},
        status = 200,
        mimetype="application/json"
    )


@Task.route('/id/addkeyword', methods=['PUT'])
def add_keyword(id):
    data = request.get_json()
    mongo.db.project.update_one(
        {'_id': ObjectId(id)}, {'$push': {"keywords": data}})
    result = mongo.db.keyword.insert_one(data)
    return Response(
        response={'message': 'Project' + id + 'Updated Team Member Successfuly:' + str(result.inserted_id)},
        status = 200,
        mimetype="application/json"
    )


@Task.route('/', methods=['GET'])
def get_tasks():
    Tasks = mongo.db.task.find()
    data = json_util.dumps(Tasks)
    return Response(
            response=data,
            status = 200,
            mimetype="application/json"
        )


@Task.route('/<id>', methods=['GET'])
def get_task(id):
    Task = mongo.db.task.find_one({'_id': ObjectId(id), })
    data = json_util.dumps(Task)
    return Response(
            response=data,
            status = 200,
            mimetype="application/json"
        )


@Task.route('/<id>', methods=['DELETE'])
def delete_task(id):
    mongo.db.task.delete_one({'_id': ObjectId(id)})
    return Response(
            response={'message': 'Task' + id + ' Deleted Successfully'},
            status = 200,
            mimetype="application/json"
        )

@Task.route('/<id>', methods=['PUT'])
def update_task(id):
    data = request.get_json()
    ReferenceTask = TaskRepo.from_dict(data)
    if ReferenceTask:
        mongo.db.task.update_one(
            {'_id': ObjectId(id)}, {'$set': ReferenceTask.to_dict()})
        return Response(
            response={'message': 'Task' + id + 'Updated Successfuly'},
            status = 200,
            mimetype="application/json"
        )
    else:
        abort(404)