from flask import Flask, render_template, url_for, redirect, request, session
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
        return redirect(url_for("userPage"))
    else:
        return render_template("loginForm.html")


@app.route("/userPage")
def userPage():
    print(session)
    if "userval" in session:
        username = session["userval"]
        return render_template("header.html",cont=f"Session Logged by {username}")


@app.route("/logout")
def logout():
    session.pop("userval",None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)



