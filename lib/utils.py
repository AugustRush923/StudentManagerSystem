import json
from db.student import Student


class StudentJSONEncoder(json.JSONEncoder):
    def default(self, o):
        return {'name': o.name, 'gender': o.gender, 'tel': o.tel}


class StudentJSONDecoder(json.JSONDecoder):
    def decode(self, s):
        dict_data = json.loads(s)
        return [Student(**student) for student in dict_data]
