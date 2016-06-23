import unittest

import markdown


class TestFormat(unittest.TestCase):

    def test_header(self):
        test = ("# Header 1\n"
                "\n"
                "   #### Header2  poipoi")

        result = markdown.convert(test)

        expected = ("<h1>Header 1</h1>\n"
                    "<h4>Header2  poipoi</h4>")

        self.assertEqual(result, expected)

    def test_paragraph(self):
        test = ("Some line\n"
                " second line\n"
                "Last line\n")

        result = markdown.convert(test)

        expected = ("<p>Some line\n"
                    "second line\n"
                    "Last line</p>")

        self.assertEqual(result, expected)

    def test_unordered_list(self):
        test = ("- first item\n"
                "-  second item\n")

        result = markdown.convert(test)

        expected = ("<ul>\n"
                    "<li>first item</li>\n"
                    "<li>second item</li>\n"
                    "</ul>")

        self.assertEqual(result, expected)

    def test_ordered_list(self):
        test = ("1. first item\n"
                "2.  second item\n"
                "10. third item\n")

        result = markdown.convert(test)

        expected = ("<ol>\n"
                    "<li>first item</li>\n"
                    "<li>second item</li>\n"
                    "<li>third item</li>\n"
                    "</ol>")

        self.assertEqual(result, expected)


class TestFormatError(unittest.TestCase):

    def test_unordered_list_elements(self):
        test = ("- first item\n"
                "second item\n")

        with self.assertRaises(markdown.FormatError) as err:
            markdown.convert(test)

        self.assertEqual(str(err.exception),
                         'Invalid line "second item" in an unordered list')


class TestComplete(unittest.TestCase):

    def test(self):
        test = ["# title title  ",
                "",
                "   ### header3",
                "",
                "- unorderedlist1",
                "- unorderedlist2",
                "- unorderedlist3",
                "",
                "1. orderlist1",
                "2. orderlist2",
                "",
                "p1",
                "p1",
                "p1",
                "",
                "p2",
                "# poipoi",
                ""]

        result = markdown.convert('\n'.join(test))

        expected = ["<h1>title title</h1>",
                    "<h3>header3</h3>",
                    "<ul>",
                    "<li>unorderedlist1</li>",
                    "<li>unorderedlist2</li>",
                    "<li>unorderedlist3</li>",
                    "</ul>",
                    "<ol>",
                    "<li>orderlist1</li>",
                    "<li>orderlist2</li>",
                    "</ol>",
                    "<p>p1",
                    "p1",
                    "p1</p>",
                    "<p>p2",
                    "# poipoi</p>"]

        self.assertEqual(result.splitlines(), expected)
