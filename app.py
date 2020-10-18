#!flask/bin/python3
from flask import Flask, jsonify, abort, make_response
# from flask_caching import Cache
# import tkinter as tk
# from tkinter import *
import requests

# interface=Tk()
# texte=Label(interface, text='API REST Fibonacci !', fg='red')
# texte.pack()
# entree = tk.Entry(interface, width=30)
# entree.pack()
#
#
# def fibo_tk():
#     nb = str(int(entree.get()))
#     print(nb)
#     response = requests.get("http://0.0.0.0:5000/fibonacci/api/v1.0/nombres/"+ nb)
#     print(response)
#     rep = json.loads(response.content)
#     print(rep)
#     variable_modifiable.set("Result : "+ str(rep["Fibonacci"]))

# boutton = Button(interface, text = 'Calculer nombre fibonacci', command = fibo_tk)
# boutton.pack()
# boutton2=Button(interface, text='Quitter', command=interface.destroy)
# boutton2.pack()
# interface.mainloop()

app = Flask(__name__)
#cache = Cache(app, config={'CACHE_TYPE': 'simple'})
#cache.init_app(app)

@app.route('/fibonacci/api/v1.0/nombres/<int:nb>', methods=['GET'])
def web_fibonacci(nb):
    #NombreFibo=fibonacci(nb)
    #cache.set(str(nb),NombreFibo)
    #r=cache.get("nb")
    #for k in cache.cache._cache:
    #    print(k, cache.get(k))
    return jsonify({'Fibonacci': fibonacci(nb)})

def fibonacci(nb):
    if(nb <= 1):
            return nb
    else:
            return (fibonacci(nb-1) + fibonacci(nb-2))

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True)
