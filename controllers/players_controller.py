from flask import render_template, Flask, redirect, request, Blueprint
from models.player import Player
from repositories import league_repository, player_repository, team_repository
players_blueprint = Blueprint("players", __name__)


@players_blueprint.route("/players")
def players():
    players = player_repository.select_all()
    return render_template("players/index.html", all_players=players)


@players_blueprint.route("/players/new", methods=["GET"])
def add_new_player():
    teams = team_repository.select_all()
    return render_template("/players/new.html", all_teams=teams)


@players_blueprint.route("/players", methods=['POST'])
def create_player():
    player_name = request.form["player_name"]
    player_fouls = request.form["fouls"]
    player_goals = request.form["goals"]
    team_id = request.form["team_id"]
    team = team_repository.select(team_id)
    player = Player(player_name, player_fouls, player_goals, team)
    player_repository.save(player)
    return redirect("/players")


@players_blueprint.route("/players/<id>/delete", methods=["POST"])
def delete_player(id):
    player_repository.delete(id)
    return redirect("/players")


@players_blueprint.route("/players/<id>/edit")
def edit_player(id):
    player = player_repository.select(id)
    team = team_repository.select_all()
    return render_template("players/edit.html", player=player, all_teams=team)


@players_blueprint.route("/players/<id>", methods=["POST"])
def update_player(id):
    player = request.form["player_name"]
    fouls = request.form["fouls"]
    goals = request.form["goals"]
    team = request.form["team_id"]
    player = Player(player, fouls, goals, team, id)
    player_repository.update(player)
    return redirect("/players")
