import unittest
from sw_journey_planner.swapi import _create_starship


class TestSwapiCreate(unittest.TestCase):
    def test_create(self):
        starship_json = ({
            "name": "Executor",
            "model": "Executor-class star dreadnought",
            "manufacturer": "Kuat Drive Yards, Fondor Shipyards",
            "cost_in_credits": "1143350000",
            "length": "19000",
            "max_atmosphering_speed": "n/a",
            "crew": "279144",
            "passengers": "38000",
            "cargo_capacity": "250000000",
            "consumables": "6 years",
            "hyperdrive_rating": "2.0",
            "MGLT": "40",
            "starship_class": "Star dreadnought",
            "pilots": [],
            "films": [
                "https://swapi.co/api/films/2/",
                "https://swapi.co/api/films/3/"
            ],
            "created": "2014-12-15T12:31:42.547000Z",
            "edited": "2017-04-19T10:56:06.685592Z",
            "url": "https://swapi.co/api/starships/15/"
        })

        starship = _create_starship(starship_json)

        with self.subTest("mglt equals 40"):
            self.assertEqual(40, starship._mglt)

        with self.subTest("consumables equals 52560"):
            self.assertEqual(52560, starship._consumables)

        with self.subTest("name is Executor"):
            self.assertEqual(40, starship._mglt)