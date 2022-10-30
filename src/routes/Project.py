import sys

from bson import json_util
from bson.objectid import ObjectId
from flask import Blueprint, abort, jsonify, make_response, request

from decorators import wrap_response
from models.Person import Person as PersonRepo
from models.Project import Project as ProjectRepo
from models.Task import Task as TaskRepo
from mongodb import mongo

Project = Blueprint("project", __name__, url_prefix="/project")


@Project.route("/", methods=["POST"])
@wrap_response
def create_project():
    data = request.get_json()
    ReferenceProject = ProjectRepo.from_dict(data)
    if ReferenceProject:
        result = mongo.db.project.insert_one(ReferenceProject.to_dict())
        ReferenceProject._id = str(result.inserted_id)
        return make_response(
            jsonify({"message": f"project created id: {result.inserted_id!r}"}), 200
        )
    else:
        abort(404)


@Project.route("/<id>/addtask/<taskid>", methods=["PUT"])
@wrap_response
def add_task(id, taskid):
    mongo.db.project.update_one(
        {"_id": ObjectId(id)}, {"$push": {"tasks": ObjectId(taskid)}}
    )
    return make_response(
        jsonify({"message": "Project" + id + "Updated Task Successfuly"}), 200
    )


@Project.route("/<id>/addteammenber/<personid>", methods=["PUT"])
def add_team_member(id, personid):
    mongo.db.project.update_one(
        {"_id": ObjectId(id)}, {"$push": {"teams": ObjectId(personid)}}
    )
    return make_response(
        jsonify({"message": "Project" + id + "Updated Team Member Successfuly"}), 200
    )


@Project.route("/<id>/deletetask/<taskid>", methods=["DELETE"])
def delete_task(id, taskid):
    mongo.db.project.update_one(
        {"_id": ObjectId(id)}, {"$pull": {"tasks": ObjectId(taskid)}}
    )
    return make_response(
        jsonify({"message": "Project" + id + "Deleted Task Successfuly"}), 200
    )


@Project.route("/<id>/deleteteammenber/<personid>", methods=["DELETE"])
def delete_team_member(id, personid):
    mongo.db.project.update_one(
        {"_id": ObjectId(id)}, {"$pull": {"teams": ObjectId(personid)}}
    )
    return make_response(
        jsonify({"message": "Project" + id + "Deleted Team Member Successfuly"}), 200
    )


@Project.route("/", methods=["GET"])
def get_projects():
    persons = mongo.db.project.find()
    data = json_util.dumps(persons)
    return make_response(jsonify({"message": data}), 200)


@Project.route("/detailed", methods=["GET"])
def get_projects_with_detail():
    persons = mongo.db.project.find()
    lst = []
    for doc in persons:
        data = doc
        data["teams_detail"] = []
        data["tasks_detail"] = []
        for item in data["teams"]:
            tmp_teams = mongo.db.person.find_one(
                {
                    "_id": ObjectId(item),
                }
            )
            data["teams_detail"].append(json_util.dumps(tmp_teams))
        for item in data["tasks"]:
            tmp_tasks = mongo.db.task.find_one(
                {
                    "_id": ObjectId(item),
                }
            )
            data["tasks_detail"].append(json_util.dumps(tmp_tasks))
        lst.append(data)
    return make_response(jsonify({"message": json_util.dumps(lst)}), 200)


@Project.route("/<id>", methods=["GET"])
def get_project(id):
    person = mongo.db.project.find_one(
        {
            "_id": ObjectId(id),
        }
    )
    data = json_util.dumps(person)
    return make_response(jsonify({"message": data}), 200)


@Project.route("/<id>", methods=["DELETE"])
def delete_project(id):
    mongo.db.project.delete_one({"_id": ObjectId(id)})
    return make_response(
        jsonify({"message": "Project" + id + " Deleted Successfully"}), 200
    )


@Project.route("/<id>", methods=["PUT"])
@wrap_response
def update_project(id):
    data = request.get_json()
    ReferenceProject = ProjectRepo.from_dict(data)
    if ReferenceProject:
        mongo.db.project.update_one(
            {"_id": ObjectId(id)}, {"$set": ReferenceProject.to_dict()}
        )
        return make_response(
            jsonify({{"message": "Project" + id + "Updated Successfuly"}}), 200
        )
    else:
        abort(404)
