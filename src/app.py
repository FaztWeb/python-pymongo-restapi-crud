from flask import Flask, jsonify, request, Response
# import uuid
from flask_pymongo import PyMongo
from bson import json_util
from bson.objectid import ObjectId

from models.Model import Person
# , Project, ProjectTeams, ProjectFiles, Task, TaskNotes, RelationTask, ProjectTasks, Keyword, TaskKeywords

app = Flask(__name__)

app.secret_key = 'secretkey'

app.config['MONGO_URI'] = 'mongodb://database/pythonmongodb'

mongo = PyMongo(app)


@app.route('/', methods=['GET'])
def index():
    message = {
        'message': "OKEY FROM API",
        'status': 200
    }
    response = jsonify(message)
    response.status_code = 404
    return response


@app.route('/person', methods=['POST'])
def create_person():
    # Receiving Data
    data = request.get_json()
    ReferencePerson = Person.from_dict(data)
    # ReferencePerson.personid = uuid.uuid4()

    if ReferencePerson:
        result = mongo.db.person.insert(ReferencePerson.to_json())
        return ReferencePerson.to_json()
    else:
        return not_found()


@app.route('/person', methods=['GET'])
def get_persons():
    persons = mongo.db.person.find()
    response = json_util.dumps(persons)
    return Response(response, mimetype="application/json")


@app.route('/person/<id>', methods=['GET'])
def get_person(id):
    person = mongo.db.person.find_one({'_id': ObjectId(id), })
    response = json_util.dumps(person)
    return Response(response, mimetype="application/json")


@app.route('/person/<id>', methods=['DELETE'])
def delete_person(id):
    mongo.db.person.delete_one({'_id': ObjectId(id)})
    response = jsonify({'message': 'Person' + id + ' Deleted Successfully'})
    response.status_code = 200
    return response


@app.route('/person/<_id>', methods=['PUT'])
def update_person(id):
    # Receiving Data
    data = request.get_json()
    ReferencePerson = Person.from_dict(data)
    
    if ReferencePerson:
        mongo.db.person.update_one(
            {'_id': ObjectId(id)}, {'$set': ReferencePerson.to_json()})
        response = jsonify({'message': 'Person' + id + 'Updated Successfuly'})
        response.status_code = 200
        return response
    else:
        return not_found()


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'message': 'Resource Not Found please, ' + request.url,
        'status': 404
    }
    response = jsonify(message)
    response.status_code = 404
    return response


if __name__ == "__main__":
    app.run(debug=True, port=3000)
