from flask import Flask, jsonify, request, make_response, url_for, redirect
import requests
import json

app = Flask(__name__)

url = 'https://127.0.0.1:5000/'


@app.route('/', methods=['POST'])
def index():
    return jsonify(request.get_json())
    '''name = request.json['name']

    create_row_data = {'name': str(name)}

    response = requests.post(
        url, data=json.dumps(create_row_data),
        headers={'Content-Type': 'application/json'}
    )
    print("the response: ", response)
    return response.content'''
    


if __name__ == '__main__':
    app.run()

