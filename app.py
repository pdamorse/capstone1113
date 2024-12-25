from flask import Flask, render_template

app = Flask(__name__, template_folder='templates/')

@app.route("/")
def homepage():
    return render_template("index.html.j2", title="Hello")

@app.route("/About")
def about_us():
    return render_template("about.html.j2", title="About Us")

@app.route("/Login")
def login_page():
    return render_template("login.html.j2", title="Login")