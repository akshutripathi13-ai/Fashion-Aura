from flask import Flask, render_template, request

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return "🎉 Fashion Aura Backend Running Successfully!"

# Login route
@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    return f"✅ Login Success for {email}"

# Signup route
@app.route("/signup", methods=["POST"])
def signup():
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")
    return f"✅ Signup Success for {name} ({email})"

if _name_ == "_main_":
    app.run(debug=True)
from flask import Flask, request, jsonify, render_template
app = Flask(_name_)

