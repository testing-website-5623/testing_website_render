from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.session_key = "secret"

@app.route("/")
def home():
    return render_template("layout.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.session.method == "POST":
        sessionp["user"] = request.form["username"]
        return render_template("/profile")
    
    return render_template("login.html")

@app.route("/profile")
def profile():
    if "user" not in session:
        return redirect("/login")
    return render_template("profile.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/")