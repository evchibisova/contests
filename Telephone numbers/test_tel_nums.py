import unittest
import task_tel_nums

class TestSolution(unittest.TestCase):
    def setup_from_file(self, file_name):
        with open("data/" + file_name, "r") as data:
            return data.read().split("\n\n")

    def test_yandex_1(self):
        inp, outp = self.setup_from_file("test_yandex_1.txt")
        self.assertEqual(task_tel_nums.solution(inp), outp, msg="Yandex case 1 failed")

    def test_yandex_2(self):
        inp, outp = self.setup_from_file("test_yandex_2.txt")
        self.assertEqual(task_tel_nums.solution(inp), outp, msg="Yandex case 2 failed")

    def test_number_parser(self):
        number = task_tel_nums.numbers_parser(["+1 (342)3  -3"])[0]
        for i in number:
            with self.subTest(i=i):
                self.assertTrue(i.isdigit(), msg="{} is not a digit".format(i))

    # def test_something(self):
    #     inp, outp = self.setup_from_file("test_yandex_2.txt")
    #     self.assertEqual(task_tel_nums.solution(inp), outp, msg="Yandex case 2 failed")
