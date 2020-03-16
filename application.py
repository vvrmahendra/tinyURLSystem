from flask import Flask
import json
app = Flask(__name__)

@app.route("/")
def index():
    return ("It is just starting! \n Wait for it")

if __name__ == "__main__":
    with open('parameters.json') as f:
        parameters = json.load(f)
    app.run(host = parameters['hostIp'])