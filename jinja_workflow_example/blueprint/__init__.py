"""
Jinja workflow test bp
"""

__author__ = "Brian Balsamo"
__email__ = "Brian@BrianBalsamo.com"
__version__ = "0.0.1"


import logging

from flask import Blueprint, render_template, abort
from .pseudodb import pseudo_db


log = logging.getLogger(__name__)


BLUEPRINT = Blueprint('jinja_workflow_test', __name__,
                      template_folder='templates', static_folder='static')



@BLUEPRINT.route("/")
def root():
    return render_template("root.html", content="It works!")

@BLUEPRINT.route("/p/<int:id>")
def person(id):
    person = None
    for x in pseudo_db['people']:
        if x['id'] == id:
            person = x
    if person is None:
        abort(404)
    return render_template("person.html", person=person)
