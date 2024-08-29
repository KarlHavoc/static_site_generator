import unittest

from extract_markdown import extract_title

md = """# Tolkien Fan Club

**I like Tolkien**. Read my [first post here](/majesty) (sorry the link doesn't work yet)

> All that is gold does not glitter

## Reasons I like Tolkien"""


class TestExtractMarkdown(unittest.TestCase):

    def test_extract_title(self):
        title = extract_title(md)
        self.assertEqual(title, "Tolkien Fan Club")
