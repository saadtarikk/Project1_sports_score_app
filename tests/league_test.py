import unittest
from models.league import League


class TestLeague(unittest.TestCase):

    def setUp(self):
        self.league = League("Premier League", 5)
