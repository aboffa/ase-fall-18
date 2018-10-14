from flakon import JsonBlueprint 
from flask import Flask, request, jsonify

calc = JsonBlueprint('calc', __name__)

@calc.route('/calc/sum', methods=['GET'])
def sum():
    m = int (request.args.get('m'))
    n = int (request.args.get('n'))

    return jsonify({'result': str(m+n)})