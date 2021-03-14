from flask import Flask, render_template, redirect, url_for
from view.control_path.flaskBlueprint import mod

app = Flask(__name__)
app.register_blueprint(mod, url_prefix="/clm")

@app.route("/")
def menu():
    return "<h1>Menu Page</h1>"


@app.route("/policy")
def policy():
    return "<h1>Policy Page</h1>"

@app.route("/call")
def claimDefn():
    return redirect(url_for("claim"))


if __name__ == "__main__":
    app.run(debug=True)