# flask package
# procces response
from flask import jsonify
from flask_restful import Resource,reqparse

# mongo-engine models
from model.student import Student

class StudentApi(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',  help="'name' cannot be left blank")
    parser.add_argument('age', type=int, help="'age' cannot be left blank")
    parser.add_argument('sex',  help="'sex' cannot be left blank")
    # read all student
    def get(self):
        output = Student.objects()
        return jsonify({'result':output})
    # add new student
    def post(self):
        data = StudentApi.parser.parse_args()
        new_student = Student(name=data["name"],age=data["age"],sex=data["sex"])
        new_student.save()
        output = Student.objects()
        return jsonify({'result': output})