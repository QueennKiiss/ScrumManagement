"""
Contains the Backend of the backlog tab
"""

from flask import Blueprint
from flask import render_template

bp = Blueprint("backlog", __name__, url_prefix="/backlog")


@bp.route("/")
def show_backlog_board() -> render_template:
    """
    show the backlog page
    """
    return render_template("base.html")

