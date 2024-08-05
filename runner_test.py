import unittest
from runner import Runner
from itertools import repeat


class RunnerTests(unittest.TestCase):
    def test_walk(self):
        runner = Runner("Jack")
        for _ in repeat(None, 10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Runner("Kate")
        for _ in repeat(None, 10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner1 = Runner("Jack")
        runner2 = Runner("Kate")
        for _ in repeat(None, 10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == '__main__':
    unittest.main()
