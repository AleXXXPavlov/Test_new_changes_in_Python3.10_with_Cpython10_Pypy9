import unittest


class SyntaxTest(unittest.TestCase):
    def test_keywords(self):
        """Testing syntax of all keywords with numeric literal"""
        def test_with_keyword(test: str):
            with self.assertWarns(DeprecationWarning):
                compile(test, "", "eval")

        # def test_with_keyword_f(test: str):
        #     with warnings.catch_warnings(record=True) as w:
        #         compile(test, "", "eval")
        #     self.assertEqual(len(w), 0)

        # testing keyword - and
        test_with_keyword("0and 123")
        test_with_keyword("0and x")
        test_with_keyword("9and x")
        test_with_keyword("4.323and x")
        test_with_keyword("-4and x")

        # test_with_keyword_f("0 and 123")
        # test_with_keyword_f("0 and x")
        # test_with_keyword_f("9 and x")
        # test_with_keyword_f("4.323 and x")
        # test_with_keyword_f("-4 and x")

        # testing keyword - or
        test_with_keyword("0o5or 123")
        test_with_keyword("0b1or x")
        test_with_keyword("9or x")
        test_with_keyword("4.323or x")
        test_with_keyword("-4or x")

        # test_with_keyword_f("0o5 or 123")
        # test_with_keyword_f("0b1 or x")
        # test_with_keyword_f("9 or x")
        # test_with_keyword_f("4.323 or x")
        # test_with_keyword_f("-4 or x")

        # testing keyword - for
        test_with_keyword("[0o5for i in ()]")
        test_with_keyword("[0b1for i in ()]")
        test_with_keyword("[9for i in ()]")
        test_with_keyword("[4.323for i in ()]")
        test_with_keyword("[-4for i in ()]")

        # test_with_keyword_f("[0o5 for i in ()]")
        # test_with_keyword_f("[0b1 for i in ()]")
        # test_with_keyword_f("[9 for i in ()]")
        # test_with_keyword_f("[4.323 for i in ()]")
        # test_with_keyword_f("[-4 for i in ()]")

        # testing keyword - in
        test_with_keyword("0o5in ()")
        test_with_keyword("0b1in ()")
        test_with_keyword("9in ()")
        test_with_keyword("4.323in ()")
        test_with_keyword("-4in ()")

        # test_with_keyword_f("0o5 in ()")
        # test_with_keyword_f("0b1 in ()")
        # test_with_keyword_f("9 in ()")
        # test_with_keyword_f("4.323 in ()")
        # test_with_keyword_f("-4 in ()")


if __name__ == "__main__":
    unittest.main()
