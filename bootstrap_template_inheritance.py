from flask import Flask, render_template

app = Flask(__name__)


@app.route("/bootstrap")
def bootstrap():
    return render_template("header.html", cont="Flask Template inheritance")


if __name__ == "__main__":
    app.run(debug=True)
