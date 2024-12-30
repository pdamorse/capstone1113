from flask import Flask, render_template

app = Flask(__name__, template_folder='templates/')

@app.route("/")
def homepage():
    return render_template("index.html.j2", title="Hello")

@app.route("/About")
def about_us():
    return render_template("about.html.j2", title="About Us")

@app.route("/Login", methods=['GET', 'POST'])
def login_page():
    if request.method == 'GET':
        return render_template("login.html.j2", title="Login")
    elif request.method == 'POST':
        return ""

@app.route("/Profile")
def profile():
    return render_template("profile.html.j2", title="Profile")



