from flask import Blueprint

mod = Blueprint("flaskBlueprint",__name__)


@mod.route("/")
def blue():
    return "<h1>Blueprint Menu Page</h1>"


@mod.route("/claimpage")
def claim():
    return "<h1>Claim Page</h1>"