from flask import Flask, render_template, url_for, redirect, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "#aDwerw#"
app.permanent_session_lifetime = timedelta(minutes=10)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.sqlite3"
app.config["SQLALCHEMY_TRACE_MODIFICATIONS"] = False

db = SQLAlchemy(app)
# db model class created for table
class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    emailId = db.Column(db.String(100))
    def __init__(self, name, email):
        self.name = name
        self.emailId = email


@app.route("/")
def home():
    return redirect(url_for("login"))


@app.route("/loginPage", methods=["GET", "POST"])
def login():
    print(request.method)
    if request.method == "POST":
        session.permanent = True
        username = request.form["usernm"]
        session["userval"] = username

        record_found = users.query.filter_by(name=username).first()
        if record_found:
            session["email"] = record_found.emailId
        else:
            new_rcd = users(username, None)
            db.session.add(new_rcd)
            db.session.commit()

        flash("Login Successful...!!!", "INFO")
        return redirect(url_for("userPage"))
    else:
        if "userval" in session:
                flash("Already Logged in..")
        return render_template("loginForm.html")


@app.route("/userPage", methods=["GET", "POST"])
def userPage():
    username = None
    email = None
    if "userval" in session:
        username = session["userval"]
        print(request.form)
        if request.method == "POST":
            email = request.form["emailID"]
            session["email"] = email
            # Below code will add email in the record type later will can be used for adding in db
            record_found = users.query.filter_by(name=username).first()
            record_found.emailId = email
            print(record_found._id, record_found.name, record_found.emailId)
            db.session.commit()
            flash("Saved..!!!")
        return render_template("user.html", emailInfo=email)
    else:
        flash("You are not logged in..!!")
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    if "userval" in session:
        username=session["userval"]
        flash(f"You have been logged out by...{username}")
    session.pop("userval",None)
    session.pop("email", None)
    return redirect(url_for("login"))


@app.route("/view")
def view():
    return render_template("view.html", records=users.query.all())


if __name__ == "__main__":
    db.create_all() # if db not created then will create one
    app.run(debug=True)



