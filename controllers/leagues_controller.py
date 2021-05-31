from flask import Flask, render_template, redirect, request
from repositories import league_repository, team_repository
from flask import Blueprint
from models.league import League

leagues_blueprint = Blueprint("leagues", __name__)


@leagues_blueprint.route("/leagues")
def leagues():
    leagues = league_repository.select_all()
    return render_template("/leagues/index.html", all_leagues=leagues)


@leagues_blueprint.route("/leagues/show")
def show_teams(league):
    league = league_repository.select(league)
    teams = league_repository.teams(league)
    return render_template("/leagues/show.html", all_teams=teams, league=league)
