from flask import Flask, jsonify, request, Response

app = Flask(__name__)

# TODO
# this result var is temp and must be removed
result = [
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


@app.errorhandler(415)
def unsupported_media_type(error=None):
    message = {
        'status': 415,
        'message': 'Unsupported Media Type: ' + request.url,
    }
    response = jsonify(message)
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.status_code = 415

    return response


@app.route('/linearalgebra/api/v1.0/consistent', methods=['POST', 'OPTIONS'])
def get_tasks():
    if request.method == 'OPTIONS':
        response = Response('', status=200, mimetype='application/json')
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
        return response

    else:
        if request.headers['Content-Type'] == 'application/json':
            json = request.json
            print(json)
            #
            #   TODO
            #   matrix = json['matrix']
            #   result = someMethodToGetResult(matrix)
            #
            response = jsonify(result)
            response.headers.add('Access-Control-Allow-Origin', '*')
            # response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
            # response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
            return response
        else:
            return unsupported_media_type()


if __name__ == "__main__":
    app.run()
