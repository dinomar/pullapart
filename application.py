from flask import Flask, jsonify, render_template, request

from helpers import getInfo

# Configure application
app = Flask(__name__)

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    """Render map"""
    return render_template("index.html")


@app.route("/info", methods=["GET"])
def info():
    """Look up articles for geo"""

    if request.method == "GET":
        # check url field is valid
        if not request.args.get("url"):
            return jsonify([])

        # get page info
        results = getInfo(request.args.get("url"))
        return jsonify(results)

    else:
        return jsonify([])

#save results to db