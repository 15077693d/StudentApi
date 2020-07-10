from mongoengine import Document, StringField, IntField

class Student(Document):
    name = StringField()
    sex = StringField()
    age = IntField()