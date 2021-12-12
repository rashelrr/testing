from flask import Flask, jsonify, json, request, redirect, url_for, flash
import requests

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    print("hello!")
    return jsonify("hello world!")
    '''api_url = 'https://lioneats.herokuapp.com'
    create_row_data = {'name': "rashel"}
    r = requests.post(url=api_url, json=create_row_data)
    print("the issue: ", r.status_code, r.reason, r.text)
    return(r.text)'''


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')

