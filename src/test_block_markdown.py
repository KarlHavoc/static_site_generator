import unittest

from block_markdown import markdown_to_blocks


class TestBlockMarkdown(unittest.TestCase):

    def test_markdown_to_blocks(self):
        md_text = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
        block_text = markdown_to_blocks(md_text)
        self.assertEqual(
            block_text,
            [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                "* This is the first list item in a list block\n* This is a list item\n* This is another list item",
            ],
        )

    def test_markdown_to_blocks_with_whitespace(self):
        md_text_with_whitespace = """    # This is a heading

    This is a paragraph of text. It has some **bold** and *italic* words inside of it.    

 * This is the first list item in a list block
* This is a list item
* This is another list item  """

        block_text = markdown_to_blocks(md_text_with_whitespace)
        self.assertEqual(
            block_text,
            [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                "* This is the first list item in a list block\n* This is a list item\n* This is another list item",
            ],
        )
