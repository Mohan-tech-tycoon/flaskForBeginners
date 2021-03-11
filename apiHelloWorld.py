from flask import Flask, redirect, url_for

appn = Flask(__name__)


@appn.route("/")
def home_func():
    return "Flask Api Web Application <h1>Coding Begins</h1>"


# <pass_val> at run time values can be passed and can handle the values passed
@appn.route("/<pass_val>")
def pass_param(pass_val):
    return f"returning the value passed in url - {pass_val}"


@appn.route("/admin")
def admin():
    return redirect(url_for("home"))
    # home is function name defined inside app. It will call the home function's service


@appn.route("/pass2/<arg2>")
def pass2_func(arg2):
    return f"pass param via redirect method; content : {arg2}"


# code for calling redirect function to invoke a service by passing value for handling inside the function
@appn.route("/admin2")
def admin2():
    return redirect(url_for("pass2_func", arg2="redirect successfully..!!!"))


@appn.route("/calc/b=<a1>/c=<a2>")
def calc(a1,a2):
    calcv = a1 + a2
    return '{"calc":"'+calcv+'"}'


if __name__ == "__main__":
    appn.run(debug=True)
