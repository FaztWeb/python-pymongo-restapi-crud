from bson import json_util
from bson.objectid import ObjectId
from flask import Blueprint, abort, jsonify, make_response, request

from decorators import wrap_response
from models.Task import Task as TaskRepo
from mongodb import mongo

Task = Blueprint("task", __name__, url_prefix="/task")


@Task.route("/", methods=["POST"])
@wrap_response
def create_task():
    data = request.get_json()
    ReferenceTask = TaskRepo.from_dict(data)
    if ReferenceTask:
        result = mongo.db.task.insert_one(ReferenceTask.to_dict())
        ReferenceTask._id = str(result.inserted_id)
        return make_response(
            jsonify({"message": f"Task created id: {result.inserted_id!r}"}), 200
        )
    else:
        abort(404)


@Task.route("/<id>/addnote", methods=["PUT"])
def add_team_member(id):
    data = request.get_json()
    mongo.db.project.update_one({"_id": ObjectId(id)}, {"$push": {"notes": data}})
    return make_response(
        jsonify({"message": "Project" + id + "Updated Team Member Successfuly"}), 200
    )


@Task.route("/<id>/addkeyword", methods=["PUT"])
def add_keyword(id):
    data = request.get_json()
    mongo.db.project.update_one({"_id": ObjectId(id)}, {"$push": {"keywords": data}})
    result = mongo.db.keyword.insert_one(data)
    return make_response(
        jsonify(
            {
                "message": "Project"
                + id
                + "Updated Team Member Successfuly:"
                + str(result.inserted_id)
            }
        ),
        200,
    )


@Task.route("/", methods=["GET"])
def get_tasks():
    Tasks = mongo.db.task.find()
    data = json_util.dumps(Tasks)
    return make_response(jsonify({"message": data}), 200)


@Task.route("/<id>", methods=["GET"])
def get_task(id):
    Task = mongo.db.task.find_one(
        {
            "_id": ObjectId(id),
        }
    )
    data = json_util.dumps(Task)
    return make_response(jsonify({"message": data}), 200)


@Task.route("/<id>", methods=["DELETE"])
def delete_task(id):
    mongo.db.task.delete_one({"_id": ObjectId(id)})
    return make_response(
        jsonify({"message": "Task" + id + " Deleted Successfully"}), 200
    )


@Task.route("/<id>", methods=["PUT"])
def update_task(id):
    data = request.get_json()
    ReferenceTask = TaskRepo.from_dict(data)
    if ReferenceTask:
        mongo.db.task.update_one(
            {"_id": ObjectId(id)}, {"$set": ReferenceTask.to_dict()}
        )
        return make_response(
            jsonify({"message": "Task" + id + "Updated Successfuly"}), 200
        )
    else:
        abort(404)
