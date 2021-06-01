from flask import render_template, Flask, redirect, request, Blueprint
from models.team import Team
from repositories import league_repository, team_repository
teams_blueprint = Blueprint("teams", __name__)


@teams_blueprint.route("/teams")
def teams():
    teams = team_repository.select_all()
    leagues = league_repository.select_all()
    return render_template("teams/index.html", all_teams=teams, all_leagues=leagues)


@teams_blueprint.route("/teams/new", methods=["GET"])
def add_new_team():

    leagues = league_repository.select_all()
    return render_template("/teams/new.html", all_leagues=leagues)


@teams_blueprint.route("/teams", methods=['POST'])
def create_team():
    team_name = request.form["team_name"]
    league_id = request.form["league_id"]
    league = league_repository.select(league_id)
    team = Team(team_name, league)
    team_repository.save(team)
    return redirect("/teams")

# DELETE
# DELETE '/teams/<id>'


@teams_blueprint.route("/teams/<id>/delete", methods=['POST'])
def delete_team(id):
    team_repository.delete(id)
    return redirect('/teams')

# EDIT
# GET 'teams/<id>/edit'


@teams_blueprint.route("/teams/<id>/edit", methods=['GET'])
def edit_team(id):
    team = team_repository.select(id)
    league = league_repository.select_all()
    return render_template('teams/edit.html', team=team, all_leagues=league)

# UPDATE
# PUT '/teams/<id>'


@teams_blueprint.route("/teams/<id>", methods=['POST'])
def update_team(id):
    team_name = request.form['team_name']
    league_id = request.form['league_id']
    team = Team(team_name, league_id, id)
    team_repository.update(team)
    return redirect('/teams')


@teams_blueprint.route("/teams/<id>/players", methods=["GET"])
def show_players(id):
    team = team_repository.select(id)
    players = team_repository.players(team)
    return render_template("teams/players.html", team=team, players=players)
