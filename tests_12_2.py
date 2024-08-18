import runner_and_tournament
from runner_and_tournament import Runner, Tournament
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        Runner(name='Alex')

        for i in range(10):
            Runner.walk = 50
            self.assertEqual(Runner.walk, 50)

    def test_run(self):
        Runner(name='Pavel')

        for i in range(10):
            Runner.run = 100
            self.assertEqual(Runner.run, 100)

    def test_challenge(self):
        Runner(name='Lena')
        Runner(name='Vova')

        for i in range(10):
            Runner.walk = 50
            Runner.run = 100
            self.assertNotEqual(Runner.walk, 100)
            self.assertNotEqual(Runner.run, 50)


class TournamentTest(unittest.TestCase):
    def setUpClass(self):
        self.all_finishers = {}
        print(self.all_finishers)

    def setUp(self):
        self.runer_1 = runner_and_tournament.Runner('Усэйн', 10)
        self.runer_2 = runner_and_tournament.Runner('Андрей', 9)
        self.runer_3 = runner_and_tournament.Runner('Ник', 3)

    def tearDownClass(self):
        for i in self.all_finishers:
            print(i)

    def race_1_test(self):
        race_1 = runner_and_tournament.Tournament(90, self.runer_1, self.runer_3)
        result = race_1.start()
        print(result[list(result.keys())[-1]] == 'Ник')
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Error!')
        self.all_finishers[1] = result
        self.assertEqual(Tournament.start, 90)

    def race_2_test(self):
        race_2 = runner_and_tournament.Tournament(90, self.runer_2, self.runer_3)
        result = race_2.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Error!')
        self.all_finishers[2] = result
        self.assertEqual(Tournament.start, 90)

    def race_3_test(self):
        race_3 = runner_and_tournament.Tournament(90, self.runer_1, self.runer_2, self.runer_3)
        result = race_3.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Error!')
        self.all_finishers[3] = result
        self.assertEqual(Tournament.start, 90)

    if __name__ == "__main__":
        unittest.main()
