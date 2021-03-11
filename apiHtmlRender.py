from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/idx")
def home():
    return render_template("index.html")


@app.route("/title/<pass_param>")
def title_change(pass_param):
    return render_template("titleChange.html", title_val=pass_param)


nestList = [
    {
        "name": "Kevin",
        "age": 106,
        "eyes": 2
    },
    {
        "name": "Stuart",
        "age": 105,
        "eyes": 1
    }

]


@app.route("/stmt")
def cndStmts():
    return render_template("nativePythonHTML.html", lst=['a', 'b', 'c', 'd'], r=True, num=10, minion=nestList)


if __name__ == "__main__":
    app.run(debug=True)
