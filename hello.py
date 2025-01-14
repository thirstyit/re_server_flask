from flask import Flask, request, jsonify
import run
import asyncio
import os

app = Flask(__name__)

api_keys = [
    os.environ['SAM_TEST_API_KEY'],

]

@app.route("/result")
def re_result():
    auth = request.headers.get('X-Api-Key')
    if auth in api_keys:
        url = request.args.get('url')
        out = asyncio.run(run.run(url))
        return out, 200
    else:
        return jsonify({"message": "ERROR: Unauthorized"}), 401
    