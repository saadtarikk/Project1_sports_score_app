from db.run_sql import run_sql
from models.league import League
from models.team import Team


def save(league):
    sql = "INSERT INTO leagues (league_name, league_size) VALUES (%s, %s) RETURNING *"
    values = [league.league_name, league.league_size]
    results = run_sql(sql, values)
    id = results[0]['id']
    league.id = id
    return league


def select_all():
    leagues = []
    sql = "SELECT * FROM leagues"
    results = run_sql(sql)
    for row in results:
        league = League(row['league_name'], row['league_size'], row['id'])
        leagues.append(league)
    return leagues


def select(id):
    league = None
    sql = "SELECT * FROM leagues WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        league = League(result['league_name'],
                        result['league_size'], result['id'])
    return league


def delete_all():
    sql = "DELETE FROM leagues"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM leagues WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def teams(league):
    teams = []
    sql = "SELECT * FROM teams WHERE league_id = %s"
    values = [league.id]
    results = run_sql(sql, values)

    for row in results:
        team = Team(row['team_name'], row['league_id'], row['id'])
        teams.append(team)
    return teams
