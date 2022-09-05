from flask import Blueprint, jsonify, request, Response, abort
from bson import json_util
from bson.objectid import ObjectId
from mongodb import mongo
from models.Project import Project as ProjectRepo
from models.Task import Task as TaskRepo
from models.Person import Person as PersonRepo


Project = Blueprint('project', __name__, url_prefix="/project")


@Project.route('/', methods=['POST'])
def create_project():
    data = request.get_json()
    ReferenceProject = ProjectRepo.from_dict(data)
    if ReferenceProject:
        result = mongo.db.project.insert_one(ReferenceProject.to_dict())
        ReferenceProject._id = str(result.inserted_id)
        return Response(
            response={"message": f"project created id: {str(result.inserted_id)}"},
            status = 200,
            mimetype="application/json"
        )
    else:
        abort(404)


@Project.route('/id/addtask/taskid', methods=['POST'])
def add_task(id, taskid):
    mongo.db.project.update_one(
        {'_id': ObjectId(id)}, {'$push': {"teams": ObjectId(taskid)}})
    return Response(
        response={'message': 'Project' + id + 'Updated Task Successfuly'},
        status = 200,
        mimetype="application/json"
    )


@Project.route('/id/addteammenber/personid', methods=['POST'])
def add_team_member(id, personid):
    mongo.db.project.update_one(
        {'_id': ObjectId(id)}, {'$push': {"tasks": ObjectId(personid)}})
    return Response(
        response={'message': 'Project' + id + 'Updated Team Member Successfuly'},
        status = 200,
        mimetype="application/json"
    )


@Project.route('/id/deletetask/taskid', methods=['DELETE'])
def delete_task(id, taskid):
    mongo.db.project.update_one(
        {'_id': ObjectId(id)}, {'$pull': {"teams": ObjectId(taskid)}})
    return Response(
        response={'message': 'Project' + id + 'Deleted Task Successfuly'},
        status = 200,
        mimetype="application/json"
    )


@Project.route('/id/deleteteammenber/personid', methods=['DELETE'])
def delete_team_member(id, personid):
    mongo.db.project.update_one(
        {'_id': ObjectId(id)}, {'$pull': {"tasks": ObjectId(personid)}})
    return Response(
        response={'message': 'Project' + id + 'Deleted Team Member Successfuly'},
        status = 200,
        mimetype="application/json"
    )


@Project.route('/', methods=['GET'])
def get_projects():
    persons = mongo.db.project.find()
    data = json_util.dumps(persons)
    return Response(
            response=data,
            status = 200,
            mimetype="application/json"
        )


@Project.route('/<id>', methods=['GET'])
def get_project(id):
    person = mongo.db.project.find_one({'_id': ObjectId(id), })
    data = json_util.dumps(person)
    return Response(
            response=data,
            status = 200,
            mimetype="application/json"
        )


@Project.route('/<id>', methods=['DELETE'])
def delete_project(id):
    mongo.db.project.delete_one({'_id': ObjectId(id)})
    return Response(
            response={'message': 'Project' + id + ' Deleted Successfully'},
            status = 200,
            mimetype="application/json"
        )

@Project.route('/<id>', methods=['PUT'])
def update_project(id):
    data = request.get_json()
    ReferenceProject = ProjectRepo.from_dict(data)
    if ReferenceProject:
        mongo.db.project.update_one(
            {'_id': ObjectId(id)}, {'$set': ReferenceProject.to_dict()})
        return Response(
            response={'message': 'Project' + id + 'Updated Successfuly'},
            status = 200,
            mimetype="application/json"
        )
    else:
        abort(404)