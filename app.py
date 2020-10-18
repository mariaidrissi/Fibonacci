#!flask/bin/python3
from flask import Flask, jsonify, abort, make_response

import back

app = Flask(__name__)

@app.route('/fibonacci/api/v1.0/nombres/<int:nb>', methods=['GET'])
def web_fibonacci(nb):
    return jsonify({'Fibonacci': back.fibonacci(nb)})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True)
