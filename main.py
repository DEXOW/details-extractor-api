from flask import Flask, jsonify, request 
from dotenv import load_dotenv
from src.extractor import DetailsExtractor

import os

server = Flask(__name__)

@server.route("/", methods=["GET"])
def app():
    return "Details Extractor", 200

@server.route("/extract", methods=["POST"])
def extract():
    data = request.get_json()
    if data is None:
        return "invalid request", 401
    
    try :
        extractor = DetailsExtractor(data["text"])
        return jsonify(extractor.extract())
    
    except Exception as e:
        return str(e), 500

if __name__ == "__main__":
    load_dotenv()
    if os.getenv("ENVIRONMENT") == "dev":
        print("Environment: dev")
        server.run(debug=True)
    elif os.getenv("ENVIRONMENT") == "prod":
        print("Environment: prod")
        server.run()