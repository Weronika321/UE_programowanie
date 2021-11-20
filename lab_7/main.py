from flask import Flask
from flask_restful import Api
from classes.JSON_to_API import JSON_to_API


app = Flask(__name__)
api = Api(app)


api.add_resource(JSON_to_API, "/")

if __name__ == "__main__":
    app.run(debug=True)
