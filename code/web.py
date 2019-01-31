from flask import (
    Flask, render_template
)

app = Flask(__name__, template_folder="templates")



@app.route('/')
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template("about.html")

app.run(port=8888)

