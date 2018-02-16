"""
jinja_workflow_example: A repository for testing jinja focused workflows with a dedicated front end team
"""

from flask import Flask, jsonify
from .blueprint import BLUEPRINT, __version__, __author__, __email__
from .blueprint.exceptions import Error


app = Flask(__name__)


@app.errorhandler(Error)
def handle_errors(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


app.register_blueprint(BLUEPRINT)
