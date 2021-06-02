from controllers.teams_controller import teams
from flask import Flask, render_template, redirect, request
from repositories import league_repository, team_repository, fixture_repository
from flask import Blueprint
from models.fixture import Fixture
import pdb

fixtures_blueprint = Blueprint("fixtures", __name__)


@fixtures_blueprint.route("/fixtures_list")
def fixtures():
    fixtures = fixture_repository.select_all()
    teams = team_repository.select_all()
    return render_template("fixtures/fixtures_list.html", all_fixtures=fixtures, teams=teams)


@fixtures_blueprint.route("/fixtures")
def fixtures_maintainance():
    fixtures = fixture_repository.select_all()
    teams = team_repository.select_all()
    return render_template("fixtures/index.html", all_fixtures=fixtures, teams=teams)


@fixtures_blueprint.route("/fixtures/new", methods=["GET"])
def new_fixture():
    teams = team_repository.select_all()
    leagues = league_repository.select_all()
    return render_template("fixtures/new.html", all_teams=teams, all_leagues=leagues)


@fixtures_blueprint.route("/fixtures", methods=["POST"])
def create_fixture():
    home_team = request.form["home_team"]
    away_team = request.form["away_team"]
    fixture_date = request.form["fixture_date"]
    fixture_result = request.form["fixture_result"]
    league_id = request.form["league_id"]
    fixture = Fixture(home_team, away_team, fixture_date,
                      fixture_result, league_id)
    fixture_repository.save(fixture)
    return redirect("/fixtures")


@fixtures_blueprint.route("/fixtures/<id>/delete", methods=["POST"])
def delete_fixture(id):
    fixture_repository.delete(id)
    return redirect('/fixtures')


@fixtures_blueprint.route("/fixtures/<id>/edit", methods=['GET'])
def edit_fixture(id):
    fixture = fixture_repository.select(id)
    home_team = team_repository.select(fixture.home_team)
    away_team = team_repository.select(fixture.away_team)
    teams = team_repository.select_all()
    return render_template('fixtures/edit.html', fixture=fixture, home_team=home_team, away_team=away_team, teams=teams)


@fixtures_blueprint.route("/fixtures/<id>", methods=['POST'])
def update_fixture(id):
    home_team = request.form['home_team']
    away_team = request.form['away_team']
    fixture_date = request.form['fixture_date']
    fixture_result = request.form['fixture_result']
    league_id = 1
    fixture = Fixture(home_team, away_team,
                      fixture_date, fixture_result, league_id, id)
    fixture_repository.update(fixture)
    return redirect('/fixtures')


@fixtures_blueprint.route("/fixtures_list/<id>/team_fixtures", methods=["GET"])
def show_team_fixtures(id):
    fixtures = fixture_repository.select_all()
    teams = team_repository.select_all()
    return render_template("fixtures/team_fixtures.html", fixtures=fixtures, teams=teams, team_name=id)
