'''import requests

response = requests.post("https://rashelserver.herokuapp.com", data={"name": "rashely"})
print(response.status_code)
print(response.text)
'''


from flask import Flask, jsonify, json, request, redirect, url_for, flash
import requests

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():

    url = 'https://rashelserver.herokuapp.com'
    data = {"name": "rashel"}
    r = requests.post(url=url, json=data)
    print("the response: ", r.status_code, r.reason, r.text)

    return r.text
    # this works too 1:52pm
    # return json.dumps(response.json())




@app.route('/ignore', methods=['GET'])
def ignore():
    # this works! when / in app.py is 'GET' and return jsonify({'tasks': tasks})
    url = 'https://rashelserver.herokuapp.com'

    response = requests.get(url)

    print(str(response))
    print('')
    print(json.dumps(response.json(), indent=4))
    return jsonify(response.text)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')

