from flask import render_template, Flask, redirect, request, Blueprint
from models.player import Player
from repositories import player_repository
players_blueprint = Blueprint("players", __name__)


@players_blueprint.route("/players")
def players():
    players = player_repository.select_all()
    return render_template("players/index.html", all_players=players)


@players_blueprint.route("/players/new", methods=["GET"])
def add_new_player():
    return render_template("/players/new.html")
