import sys
from flask import Flask, jsonify, request, Response
# import uuid
from flask_pymongo import PyMongo
from bson import json_util
from bson.objectid import ObjectId
from mongodb import mongo
from routes.Person import Person
from routes.Project import Project

app = Flask(__name__)

app.secret_key = 'secretkey'

app.config['MONGO_URI'] = 'mongodb://database/pythonmongodb'

# mongo = PyMongo(app)

mongo.init_app(app)

app.register_blueprint(Person)
app.register_blueprint(Project)


@app.route('/', methods=['GET'])
def index():
    return Response(
        response = "OKEY FROM API",
        status = 200,
        mimetype ="application/json"
    )

@app.errorhandler(404)
def not_found(error=None):
    return Response(
            response={'Resource Not Found please, ' + request.url},
            status = 404,
            mimetype="application/json"
        )


if __name__ == "__main__":
    app.run(debug=True, port=3000)
