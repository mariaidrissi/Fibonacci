#!flask/bin/python
from flask import Flask, jsonify, abort, make_response
from flask_caching import Cache

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
cache.init_app(app)

@app.route('/fibonacci/api/v1.0/nombres/<int:nb>', methods=['GET'])
def web_fibonacci(nb):
    NombreFibo=fibonacci(nb)
    cache.set(str(nb),NombreFibo)
    r=cache.get("nb")
    for k in cache.cache._cache:
        print(k, cache.get(k))
    return jsonify({'Fibonacci': fibonacci(nb)})

def fibonacci(nb):
    if(nb <= 1):
            return nb
    else:
            return (fibonacci(nb-1) + fibonacci(nb-2))

def inv_fibonacci(k):
    if(k <= 1):
        return k
    else:
        return (inv_fibonacci(k)-inv_fibonacci(k-1))

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)
