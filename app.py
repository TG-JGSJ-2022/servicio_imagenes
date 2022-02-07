from flask import Flask, request
import cv2

from Services.stringtoimage import imageb64_to_CV2

app = Flask(__name__)


@app.route("/")
def index():
    return "hola mundo"

@app.route("/Rescale", methods=["POST","OPTIONS"])
def Rescale():
    r = request.get_json()
    image = imageb64_to_CV2(r["imagen_64"])
    return "hola"

app.run(debug=True,
        port = 5000,
        host="0.0.0.0")
    

