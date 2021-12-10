from Application import *
from flask import Flask, redirect, url_for, render_template, request, flash

app = Flask(__name__,static_url_path='', static_folder='static', template_folder='templates')

@app.route("/")
def rootRoute():
    print("root route")
    return render_template("index.html")

@app.route("/igdtuw")
def index():
    print("root route")
    application()
    return render_template("end.html")
    return "OK"

if __name__ == "__main__":
    app.run(debug=True)