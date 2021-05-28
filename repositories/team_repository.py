from repositories import league_repository
from db.run_sql import run_sql
from models.team import Team
from models.player import Player


def save(team):
    sql = "INSERT INTO teams (team_name, league_id) VALUES (%s, %s) RETURNING*"
    values = [team.team_name, team.league_id.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    team.id = id
    return team


def select_all():
    teams = []
    sql = "SELECT * FROM teams"
    results = run_sql(sql)

    for row in results:
        league = league_repository.select(row['league_id'])
        team = Team(row['team_name'], league, row['id'])
        teams.append(team)
    return teams


def select(id):
    team = None
    sql = "SELECT * FROM teams WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        league = league_repository.select(result['league_id'])
        team = Team(result['team_name'], league, result['id'])
    return team


def delete_all():
    sql = "DELETE FROM teams"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM teams WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(team):
    sql = "UPDATE teams SET (team_name, league_id) = (%s, %s) WHERE id = %s"
    values = [team.team_name, team.league_id.id]
    run_sql(sql, values)


def players(team):
    players = []
    sql = "SELECT * FROM players WHERE team_id = %s"
    values = [team.id]
    results = run_sql(sql, values)

    for row in results:
        player = Player(row['player_name'], row['fouls'],
                        row['goals'], row['team_id'], row['id'])
        players.append(player)
    return players
