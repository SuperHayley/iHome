# -*- coding:utf-8 -*-
# 程序入口

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return 'index'

if __name__ == "__main__":
    app.run(debug=True)