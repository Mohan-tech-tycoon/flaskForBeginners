from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return "Home Page"


@app.route("/login", methods=["POST", "GET"])
def login_page():
    print(request.form)
    if request.method == "POST":
        username = request.form["usernm"]
        return redirect(url_for("user_page", usr=username))
    else:
        return render_template("loginForm.html")


@app.route("/<usr>")
def user_page(usr):
    return render_template("header.html", cont=usr)


if __name__ == "__main__":
    app.run(debug=True)