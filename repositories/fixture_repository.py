from typing import ValuesView

from db.run_sql import run_sql
from models.league import League
from models.team import Team
from models.fixture import Fixture


def save(fixture):
    sql = "INSERT INTO fixtures (home_team, away_team, fixture_date, fixture_result, league_id) VALUES (%s, %s, %s, %s, %s) RETURNING id "
    values = [fixture.home_team, fixture.away_team, fixture.fixture_date,
              fixture.fixture_result, fixture.league_id]
    results = run_sql(sql, values)
    id = results[0]['id']
    fixture.id = id
    return fixture


def select_all():
    fixtures = []
    sql = "SELECT * FROM fixtures"
    results = run_sql(sql)
    for row in results:
        fixture = Fixture(row['home_team'], row['away_team'], row['fixture_date'],
                          row['fixture_result'], row['league_id'], row['id'])
        fixtures.append(fixture)
    return fixtures


def select(id):
    fixture = None
    sql = "SELECT * FROM fixture WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        fixture = Fixture(result['home_team'], result['away_team'], result['fixture_date'],
                          result['fixture_result'], result['league_id'], result['id'])
    return fixture


def delete_all():
    sql = "DELETE FROM fixtures"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM fixtures WHERE id = %s"
    values = id
    run_sql(sql, values)


def update(fixture):
    sql = "UPDATE fixtures SET (home_team, away_team, fixture_location, fixture_result, league_id) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [fixture.home_team, fixture.away_team,
              fixture.fixture_location, fixture.fixture_result, fixture.league_id]
    run_sql(sql, values)
