from flask import Flask, render_template, request
import numpy as np
import plotly.graph_objects as go
import plotly.io as pio

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
    

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/Projects")
def Projects():
    return render_template("Projects.html")



if __name__ == "__main__":
    app.run(debug=True)