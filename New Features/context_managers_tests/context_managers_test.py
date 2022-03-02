import unittest


class Example:
    def __init__(self, check):
        self.check = check

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

class GeneralCase(unittest.TestCase):
    def test_with_files(self):
        """
        Simple testing new opportunity of several context managers with open
        """

        with (
            open("date/example1.txt", encoding="locale", mode="w") as file1,
            open("date/example2.txt", encoding="locale", mode="w") as file2
        ):
            file1.write("0")
            file2.write("1")

        with (
            open("date/example1.txt", encoding="locale", mode="r") as file1,
            open("date/example2.txt", encoding="locale", mode="r") as file2
        ):
            self.assertEqual(file1.read(), "0")
            self.assertEqual(file2.read(), "1")

    def test_with_erros(self):
        """
        Simple testing new opportunity of several context managers with error
        """
        with (
            self.assertRaises(FileNotFoundError),
            open("notexist.txt", mode="r", encoding="locale") as file
        ):
            pass

    def test_with_class(self):
        """
        Simple testing new opportunity of several context managers with class
        """
        tp_save: tuple[int, int] = ()
        with (
            Example(1) as exc1,
            Example(2) as exc2
        ):
            tp_save = (exc1.check, exc2.check)

        self.assertEqual(tp_save, (1, 2))



    def test_hard(self):
        """
        Simple testing new opportunity of several context managers with many errors
        """

        with (
            self.assertRaises(ZeroDivisionError) as main_ass,
            open("date/example1.txt", mode="r", encoding="locale") as file,
            open("date/example1.txt", mode="r", encoding="locale") as file,
            open("date/example1.txt", mode="r", encoding="locale") as file,
            open("date/example1.txt", mode="r", encoding="locale") as file,
            open("date/example1.txt", mode="r", encoding="locale") as file,
            open("date/example1.txt", mode="r", encoding="locale") as file
        ):
            check = 1 / 0





if __name__ == '__main__':
    unittest.main()
