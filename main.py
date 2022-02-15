import cv2
from flask import Flask, make_response, redirect, render_template, request, flash
import numpy as np
import Utils.resize_image as ri

app = Flask(__name__)

"""---------------------------
            Routes
---------------------------"""
@app.route("/")
def index():
    return "hola mundo"
# Eod

@app.route("/resize", methods=["POST", "GET"])
def resize_image():

    # -------------------------
    #       GET method
    # -------------------------
    if request.method == "GET":
        return render_template("index.html")
    # Eoi

    # -------------------------
    #      POST method
    # -------------------------
    # Check if the image is in the request
    if "image" not in request.files:
        flash("File not found in request")
        return redirect(request.url)
    # Eoi

    # Get image from request
    image_from_request = request.files["image"]

    # Pre process image
    image_array = np.frombuffer(image_from_request.read(), np.uint8)
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

    # Process image
    # resized_image = ri.image_resize_dominant_color(image)
    resized_image = ri.image_resize_average_color(image)

    # Return resized image
    _, buffer = cv2.imencode(".png", resized_image)
    response = make_response(buffer.tobytes())
    response.content_type = "image/png"
    return response
# Eod