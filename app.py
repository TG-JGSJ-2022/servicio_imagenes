from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "hola mundo"

@app.route("/resize")
def resize_image():
    return "Resize image"

app.run(debug=True,
        port = 5000,
        host="0.0.0.0")
