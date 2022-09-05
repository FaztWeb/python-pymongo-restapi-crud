from bson import json_util
from bson.objectid import ObjectId
from flask import Blueprint, abort, jsonify, make_response, request

from models.Person import Person as PersonRepo
from mongodb import mongo

Person = Blueprint("person", __name__, url_prefix="/person")


@Person.route("/", methods=["POST"])
def create_person():
    data = request.get_json()
    ReferencePerson = PersonRepo.from_dict(data)
    if ReferencePerson:
        result = mongo.db.person.insert_one(ReferencePerson.to_dict())
        ReferencePerson._id = str(result.inserted_id)
        return make_response(
            jsonify({"message": f"person created id: {result.inserted_id!r}"}), 200
        )
    else:
        abort(404)


@Person.route("/", methods=["GET"])
def get_persons():
    persons = mongo.db.person.find()
    data = json_util.dumps(persons)
    return make_response(jsonify({"message": data}), 200)


@Person.route("/<id>", methods=["GET"])
def get_person(id):
    person = mongo.db.person.find_one(
        {
            "_id": ObjectId(id),
        }
    )
    data = json_util.dumps(person)
    return make_response(jsonify({"message": data}), 200)


@Person.route("/<id>", methods=["DELETE"])
def delete_person(id):
    mongo.db.person.delete_one({"_id": ObjectId(id)})
    return make_response(
        jsonify({"message": "Person" + id + " Deleted Successfully"}), 200
    )


@Person.route("/<id>", methods=["PUT"])
def update_person(id):
    data = request.get_json()
    ReferencePerson = PersonRepo.from_dict(data)
    if ReferencePerson:
        mongo.db.person.update_one(
            {"_id": ObjectId(id)}, {"$set": ReferencePerson.to_dict()}
        )
        return make_response(
            jsonify({"message": "Person" + id + "Updated Successfuly"}), 200
        )
    else:
        abort(404)
