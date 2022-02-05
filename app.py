from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    return "hola mundo"

@app.route("/Rescale")
def Rescale():
    r = request.get_json()

app.run(debug=True,
        port = 5000,
        host="0.0.0.0")
    

