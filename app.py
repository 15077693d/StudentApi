from flask import Flask
from flask_restful import Api
from api.student import StudentApi
from flask_mongoengine import MongoEngine
db = MongoEngine()
app = Flask(__name__)
app.config["MONGODB_HOST"] = "mongodb+srv://test:test@cluster0.yjmzp.gcp.mongodb.net/student?retryWrites=true&w=majority"
api = Api(app)
api.add_resource(StudentApi, "/student")
if __name__ == '__main__':
    db.init_app(app)
    app.run()

