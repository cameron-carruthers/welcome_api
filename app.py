from flask import Flask, request
import requests

app = Flask(__name__)


@app.route('/houses', methods=['GET'])
def get_houses():
    return 'hello world'


if __name__ == '__main__':
    app.run(debug=True)
