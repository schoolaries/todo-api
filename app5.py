#!flask/bin/python
from flask import Flask, jsonify, abort, request, make_response, url_for
import os, api5, csv, json, subprocess

mikrotik = Flask(__name__)

@mikrotik.route('/todo/api/mikrotik/createuser', methods=['POST'])
def createuser():
    name = request.json['name']
    group = request.json['group']
    password = request.json['password']

    subprocess.call(['./test.sh', 'create', name, group, password])
    with open('file.txt') as f:
	output = f.read()
    return jsonify({'name':name, 'group':group, 'password':password})


@mikrotik.route('/todo/api/mikrotik/printuser', methods=['GET'])
def getuser():
    subprocess.call(['./test.sh', 'print'])
    with open('file.txt') as f:
	output = f.read()
    return jsonify({'user': output})

@mikrotik.route('/todo/api/mikrotik/updateuser/<numbers>', methods=['PUT'])
def updateuser(numbers):
    nuser = request.json['nuser']
    group = request.json['group']
    password = request.json['password']

    subprocess.call(['./test.sh', 'update', numbers, nuser, group, password])
    with open('file.txt') as f:
	output = f.read()
    return jsonify({'user': output})

@mikrotik.route('/todo/api/mikrotik/deleteuser/<numbers>', methods=['DELETE'])
def deleteuser(numbers):
    subprocess.call(['./test.sh', 'delete', numbers])
    with open('file.txt') as f:
	output = f.read()
    return jsonify({'user': output, 'delete': True})

if __name__ == '__main__':
    mikrotik.run(debug=True)

