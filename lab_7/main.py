from flask import Flask
from flask_restful import Resource, Api
from classes.Movie_to_API import Movie_to_API
from classes.HelloWorld import HelloWorld


app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {"hello": "world"}


api.add_resource(HelloWorld, "/")
api.add_resource(Movie_to_API, "/movies")

if __name__ == "__main__":
    app.run(debug=True)
