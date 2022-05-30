from os import abort
from flask import Flask,request,jsonify
from flask.templating import render_template

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return render_template("index.html")



if __name__ == "__main__":
    app.run(port = 5000,debug = False)