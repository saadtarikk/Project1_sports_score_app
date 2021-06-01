DROP TABLE IF EXISTS fixtures;
DROP TABLE IF EXISTS players;
DROP TABLE IF EXISTS teams;
DROP TABLE IF EXISTS leagues;

CREATE TABLE leagues (
    id SERIAL PRIMARY KEY,
    league_name VARCHAR(255),
    league_size INT    
);

CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    team_name VARCHAR(255),
    league_id INT REFERENCES leagues(id)

);

CREATE TABLE players (
    id SERIAL PRIMARY KEY,
    player_name VARCHAR(255),
    fouls INT,
    goals INT,
    team_id INT REFERENCES teams(id)
);

CREATE TABLE fixtures (
    id SERIAL PRIMARY KEY,
    home_team INT REFERENCES teams(id),
    away_team INT REFERENCES teams(id),
    fixture_date DATE,
    fixture_result VARCHAR(255),
    league_id INT REFERENCES leagues(id)
);