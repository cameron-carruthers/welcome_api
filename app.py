from flask import Flask, request
import requests
import os

app = Flask(__name__)


@app.route('/houses', methods=['GET'])
def get_houses():
    API_KEY = os.getenv('API_KEY')
    headers = {'x-rapidapi-key': API_KEY,
               'x-rapidapi-host': 'realtor.p.rapidapi.com'}
    houses = requests.get(
        'https://realtor.p.rapidapi.com/properties/v2/list-for-sale', params=request.args, headers=headers)
    return houses


if __name__ == '__main__':
    app.run(debug=True)
