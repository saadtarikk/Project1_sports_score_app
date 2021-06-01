from pdb import run
from db.run_sql import run_sql
from repositories import player_repository, team_repository
from models.player import Player
from models.team import Team


def save(player):
    sql = "INSERT INTO players (player_name, fouls, goals, team_id) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [player.player_name, player.fouls,
              player.goals, player.team_id.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    player.id = id
    return player


def select_all():
    players = []
    sql = "SELECT * FROM players"
    results = run_sql(sql)
    for row in results:
        team = team_repository.select(row['team_id'])
        player = Player(row['player_name'], row['fouls'],
                        row['goals'], team, row['id'])
        players.append(player)
    return players


def select(id):
    player = None
    sql = "SELECT * FROM players WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        team = team_repository.select(result['team_id'])
        player = Player(result['player_name'], result['fouls'],
                        result['goals'], team, result['id'])
    return player


def delete_all():
    sql = "DELETE FROM players"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM players WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(player):
    sql = "UPDATE players SET (player_name, fouls, goals, team_id) = (%s, %s, %s, %s) WHERE id = %s"
    values = [player.player_name, player.fouls,
              player.goals, player.team_id, player.id]
    run_sql(sql, values)
