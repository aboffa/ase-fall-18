from flask import Flask, jsonify
from werkzeug.routing import BaseConverter, ValidationError

_USERS = {'1':'A', '2':'B', '3':'C' }
_IDS = {val: id for id,val in _USERS.items()}

class RegisteredUser(BaseConverter):
    def to_python(self,value):
        if value in _USERS:
            return _USERS[value]
        raise ValidationError()
    
    def to_url(self,value):
        return _IDS[value]

app = Flask(__name__)
app.url_map.converters['registered'] = RegisteredUser

@app.route('/api', methods = ['POST','DELETE','GET'])
def my_microservice():
    print(request)
    responce = jsonify({'Hello':'World'})
    print(responce)
    print(responce.data)
    return responce

# @app.route('/api/person/<person_id>')
# def person(person_id):
#     responce = jsonify({'Hello':person_id})
#     return responce

@app.route('/api/person/<registered:name>')
def person(name):
    responce = jsonify({'Hello' : name})
    return responce

if __name__ == '__main__':
    app.run()