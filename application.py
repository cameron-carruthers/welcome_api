from flask import Flask, request, jsonify
import requests
import os
import json

application = Flask(__name__)


@application.route('/', methods=['GET'])
def greet():
    return ('You have reached the Welcome API.  Please navigate to other endpoints to retrieve data')


@application.route('/houses', methods=['GET'])
def get_houses():
    API_KEY = os.getenv('API_KEY')
    headers = {'x-rapidapi-key': API_KEY,
               'x-rapidapi-host': 'realtor.p.rapidapi.com'}
    params = request.args.to_dict()
    houses = requests.get(
        'https://realtor.p.rapidapi.com/properties/v2/list-for-sale', params=params, headers=headers)
    return (houses.content)


@application.route('/house', methods=['GET'])
def get_house():
    API_KEY = os.getenv('API_KEY')
    headers = {'x-rapidapi-key': API_KEY,
               'x-rapidapi-host': 'realtor.p.rapidapi.com'}
    params = request.args.to_dict()
    house = requests.get(
        'https://realtor.p.rapidapi.com/properties/v2/detail', params=params, headers=headers)
    return (house.content)


if __name__ == '__main__':
    application.run(debug=True)
