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
    return render_template("/teams/new.html")


@teams_blueprint.route("/teams", methods=['POST'])
def create_team():
    team_name = request.form["team_name"]
    # league_id = 1
    team = Team(team_name, league_id)
    team_repository.save(team)
    return redirect('/teams')

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
    return render_template('teams/edit.html', team=team)

# UPDATE
# PUT '/teams/<id>'


@teams_blueprint.route("/teams/<id>", methods=['POST'])
def update_team(id):
    team_name = request.form['team_name']
    league_id = 1
    team = Team(team_name, league_id, id)
    team_repository.update(team)
    return redirect('/teams')
