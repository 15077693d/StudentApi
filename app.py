from flask import Flask
from flask_restful import Api
from api.student import StudentApi
from flask_cors import CORS
from flask_mongoengine import MongoEngine
db = MongoEngine()
app = Flask(__name__)
CORS(app)
app.config["MONGODB_HOST"] = "mongodb+srv://test:test@cluster0.yjmzp.gcp.mongodb.net/student?retryWrites=true&w=majority"
api = Api(app)
api.add_resource(StudentApi, "/student")
db.init_app(app)
if __name__ == '__main__':
    app.run()

