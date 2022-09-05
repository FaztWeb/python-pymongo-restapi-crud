from flask import Flask, jsonify, make_response, request

# import uuid
from flask_pymongo import PyMongo

from mongodb import mongo
from routes.Person import Person
from routes.Project import Project
from routes.Task import Task

app = Flask(__name__)

app.secret_key = "secretkey"

app.config["MONGO_URI"] = "mongodb://database/pythonmongodb"

# mongo = PyMongo(app)

mongo.init_app(app)

app.register_blueprint(Person)
app.register_blueprint(Project)
app.register_blueprint(Task)


@app.route("/", methods=["GET"])
def index():
    return make_response(jsonify({"message": "OKEY FROM API"}), 200)


@app.errorhandler(404)
def not_found(error=None):
    return make_response(
        jsonify({"message": "Resource Not Found please, " + request.url}), 200
    )


if __name__ == "__main__":
    app.run(debug=True, port=3000)
