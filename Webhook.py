from flask import Flask,request
from module import main
import os
import sys

app = Flask(__name__)

@app.route("/",methods=["POST","GET"])
def index():
    if request.method == "POST":
        data = request.get_json()
        main(data)
        return "200 - ok"
    else:
        return "200 - ok"

app.run(debug=True,host="0.0.0.0",port=int(os.environ.get("PORT","5000")))