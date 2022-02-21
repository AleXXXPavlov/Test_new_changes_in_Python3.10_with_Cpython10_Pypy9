import unittest


class Point:
    __match_args__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y


class MatchTest(unittest.TestCase):
    def test_simpleMatch(self):
        """Testing simple example for new pattern matching in Python"""
        param: int = 2
        match param:
            case -1 | 1:
                check = 1
            case 0:
                check = 0
            case _:
                check = -1

        self.assertEqual(check, -1)

    def test_withClass(self):
        """Testing pattern matching with classes and guard"""
        code = ""
        point = Point(1, 1)
        match point:
            case Point(0, 0):
                code = "using without capture class attributes into variables"
            case Point(0, y):
                code = "using with capture last class attribute"
            case Point(x, 0):
                code = "using with capture previous class attribute"
            case Point(x, y) if x == y:
                code = "using with capture all of class attribute when attributes are equal"
            case Point(x, y):
                code = "using with capture all of class attribute"

        self.assertRegex(code, r".*all.*equal")

    def test_complexPatterns(self):
        """Testing complex patterns"""

        # version / status code / status text / headers / body
        http_response: tuple = ("HTTP/1.1", "404", "Not Found", "Date: Mon, 14 Jul 2022 12:28:53 GMT")

        match_result = ""
        match http_response:
            case (version, code, _):
                match_result = version + " " + code
            case (version, code, *args):
                match_result = version + " " + code
                for arg in args[1:]:
                    match_result += "\n" + arg

        self.assertEqual(match_result, "HTTP/1.1 404\nDate: Mon, 14 Jul 2022 12:28:53 GMT")

    @unittest.expectedFailure
    def test_withDict(self):
        """Testing dictionary matching patterns"""
        alphabet_code = {'a': 61, 'b': 62}

        code = ""
        match alphabet_code:
            case {**alphabet} if len(alphabet) == 1:
                code = "one letter"
            case {**alphabet} if len(alphabet) == 2:
                code = "two letters"
            case {**alphabet} if len(alphabet) > 2:
                code = "more than two letters"

        self.assertEqual(code, "one letter")


if __name__ == "__main__":
    unittest.main()
