import unittest
from runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner('Усэйн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            value = {place: str(participant) for place, participant in value.items()}
            print(value)

    def test1(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        self.all_results['Усэйн и Ник'] = results

        last = results[len(results)]
        self.assertTrue(last, self.runner3)

    def test2(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results['Андрей и Ник'] = results

        last = results[len(results)]
        self.assertTrue(last, self.runner3)

    def test3(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results['Усэйн, Андрей, Ник'] = results

        last = results[len(results)]
        self.assertTrue(last, self.runner3)

    if __name__ == '__main__':
        unittest.main()
