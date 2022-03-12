from flask import Flask, request, jsonify
import requests
from flask_caching import Cache  # Import Cache from flask_caching module
import redis

app = Flask(__name__)
# Set the configuration variables to the flask application
# app.config.from_object('config.Config')
# cache = Cache(app)  # Initialize Cache


@app.route("/universities")
# @cache.cached(timeout=30, query_string=True)
def get_universities():
    API_URL = "http://universities.hipolabs.com/search?country="
    search = request.args.get('country')
    r = requests.get(f"{API_URL}{search}")
    return jsonify(r.json())


@app.route("/addinredis")
def add_key():
    API_URL = "http://universities.hipolabs.com/search?country="
    key = request.args.get('key')
    value = request.args.get('value')
    #r = requests.get(f"{API_URL}{search}")
    r = redis.Redis(
        host='http://redis-cache.cache.svc.cluster.local', port=6379, db=0)
    x = r.set(key, value)
    return jsonify(x.json())


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
