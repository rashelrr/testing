from flask import Flask, jsonify, request, make_response, url_for, redirect, abort
import requests
import json

app = Flask(__name__)

url = 'https://127.0.0.1:5000/'


tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]


@app.route('/', methods=['POST'])
def index():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201


@app.route('/ignore', methods=['GET'])
def ignore():
    return jsonify({'tasks': tasks})
    #return jsonify(request.get_json())
    #response = requests.get(url)
    #return jsonify(response.json())
    

    '''name = request.json['name']

    create_row_data = {'name': str(name)}

    response = requests.post(
        url, data=json.dumps(create_row_data),
        headers={'Content-Type': 'application/json'}
    )
    print("the response: ", response)
    return response.content'''
    


if __name__ == '__main__':
    app.run(debug=True)

