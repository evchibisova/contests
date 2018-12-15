import unittest
from task_strings_graph import solution

class TestSolution(unittest.TestCase):
    def setup_from_file(self, file_name):
        with open("data/" + file_name, "r") as data:
            return data.read().split("\n\n")

    def test_yandex_1(self):
        inp, outp = self.setup_from_file("test_yandex_1.txt")
        self.assertEqual(solution(inp), outp, msg="Yandex case 1 failed")