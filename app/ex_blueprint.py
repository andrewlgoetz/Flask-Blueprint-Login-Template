from flask import Blueprint

## This file is a template of how to setup another blueprint file, which you may place in another directory.

example_blueprint = Blueprint('example_blueprint', __name__)


@example_blueprint.route('/home')
def home():
    return "This is an example app - blueprint displayed"