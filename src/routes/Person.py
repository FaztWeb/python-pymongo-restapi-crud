from flask import Blueprint, jsonify, request, Response, abort
from bson import json_util
from bson.objectid import ObjectId
from mongodb import mongo
from models.Person import Person as PersonRepo


Person = Blueprint('person', __name__, url_prefix="/person")


@Person.route('/', methods=['POST'])
def create_person():
    data = request.get_json()
    ReferencePerson = PersonRepo.from_dict(data)
    if ReferencePerson:
        result = mongo.db.person.insert_one(ReferencePerson.to_dict())
        ReferencePerson._id = str(result.inserted_id)
        return Response(
            response={"message": f"person created id: {str(result.inserted_id)}"},
            status = 200,
            mimetype="application/json"
        )
    else:
        abort(404)


@Person.route('/', methods=['GET'])
def get_persons():
    persons = mongo.db.person.find()
    data = json_util.dumps(persons)
    return Response(
            response=data,
            status = 200,
            mimetype="application/json"
        )


@Person.route('/<id>', methods=['GET'])
def get_person(id):
    person = mongo.db.person.find_one({'_id': ObjectId(id), })
    data = json_util.dumps(person)
    return Response(
            response=data,
            status = 200,
            mimetype="application/json"
        )


@Person.route('/<id>', methods=['DELETE'])
def delete_person(id):
    mongo.db.person.delete_one({'_id': ObjectId(id)})
    return Response(
            response={'message': 'Person' + id + ' Deleted Successfully'},
            status = 200,
            mimetype="application/json"
        )

@Person.route('/<id>', methods=['PUT'])
def update_person(id):
    data = request.get_json()
    ReferencePerson = PersonRepo.from_dict(data)
    if ReferencePerson:
        mongo.db.person.update_one(
            {'_id': ObjectId(id)}, {'$set': ReferencePerson.to_dict()})
        return Response(
            response={'message': 'Person' + id + 'Updated Successfuly'},
            status = 200,
            mimetype="application/json"
        )
    else:
        abort(404)