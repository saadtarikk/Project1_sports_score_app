import pdb
from models.league import League
from models.team import Team
from models.player import Player
from models.fixture import Fixture

import repositories.league_repository as league_repository
import repositories.team_repository as team_repository
import repositories.player_repository as player_repository
import repositories.fixture_repository as fixture_repository

# fixture_repository.delete_all()
player_repository.delete_all()
team_repository.delete_all()
league_repository.delete_all()


league1 = League("Premier League", 5)
league_repository.save(league1)
league2 = League("La Liga", 5)
league_repository.save(league2)

team1 = Team("Arsenal", league1)
team_repository.save(team1)
team2 = Team("Manchester City", league1)
team_repository.save(team2)

player1 = Player("Messi", 3, 50, team1)
player2 = Player("gessi", 3, 50, team1)
player3 = Player("vessi", 3, 50, team1)

player_repository.save(player1)
player_repository.save(player2)
player_repository.save(player3)
# fixtures = fixture_repository.select_all()
pdb.set_trace()
