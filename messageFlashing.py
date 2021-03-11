from flask import Flask, render_template, url_for, redirect, request, session, flash
from datetime import timedelta


app = Flask(__name__)
app.secret_key = "#aDwerw#"
app.permanent_session_lifetime = timedelta(minutes=10)


@app.route("/")
def home():
    return redirect(url_for("login"))


@app.route("/loginPage", methods=["GET","POST"])
def login():
    print(request.method)
    if request.method == "POST":
        session.permanent = True
        username = request.form["usernm"]
        session["userval"] = username
        flash("Login Successful...!!!","INFO")
        return redirect(url_for("userPage"))
    else:
        if "userval" in session:
                flash("Already Logged in..")
        return render_template("loginForm.html")


@app.route("/userPage", methods=["GET","POST"])
def userPage():
    username = None
    if "userval" in session:
        username = session["userval"]
        return render_template("header.html",cont=username)

@app.route("/logout")
def logout():
    if "userval" in session:
        username=session["userval"]
        flash(f"You have been logged out by...{username}")
    session.pop("userval",None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)



