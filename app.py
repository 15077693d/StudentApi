from flask import Flask
from flask_restful import Api
from api.student import StudentApi
from flask_mongoengine import MongoEngine
db = MongoEngine()
app = Flask(__name__)
app.config.update(
    {'MONGODB_SETTINGS': {
        'db': 'test',
        'host': 'localhost',
        'port': 27017}})
api = Api(app)
api.add_resource(StudentApi, "/student")
if __name__ == '__main__':
    db.init_app(app)
    app.run()

