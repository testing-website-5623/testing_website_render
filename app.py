from cs50 import SQL
from flask import Flask, render_templates, redirect, request, session
from flask-session import Session

app = Flask(__name__)

db = SQL("sqlite:///users.db")

app.config["SESSION_PERMENENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")