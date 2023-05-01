"""
Contains the Backend of the backlog tab
"""

from flask import Blueprint
from flask import render_template

bp = Blueprint("backlog", __name__)


@bp.route("/")
def base_page() -> render_template:
    """
    show the backlog page
    """
    return render_template("base.html")


@bp.route("/home")
def show_home_content() -> render_template:
    """
    show the backlog page
    """
    return render_template("home.html")


@bp.route("/backlog")
def show_backlog_board() -> render_template:
    """
    show the backlog page
    """
    return render_template("backlog.html")


@bp.route("/sprint")
def show_sprint_content() -> render_template:
    """
    show the backlog page
    """
    return render_template("sprint.html")


@bp.route("/users")
def show_users_content() -> render_template:
    """
    show the backlog page
    """
    return render_template("users.html")


@bp.route("/board")
def show_board_content() -> render_template:
    """
    show the backlog page
    """
    return render_template("board.html")