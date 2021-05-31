from flask import Flask, render_template
from flask import Blueprint

admin_blueprint = Blueprint("admin", __name__)


@admin_blueprint.route("/admin")
def admin():
    return render_template("/admin/index.html")
