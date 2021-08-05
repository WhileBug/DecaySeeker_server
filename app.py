from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/getCaptcha")
def getCaptch():
    return "111111"

@app.route("/getData")
def getData():
    return None

@app.route("/getAnalysis")
def getAnalysis():
    return ""