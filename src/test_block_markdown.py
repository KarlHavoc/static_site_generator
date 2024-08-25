import unittest

from block_markdown import block_to_block_type, markdown_to_blocks


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

    def test_block_to_block_type_(self):
        paragraph_text = "This is a paragraph"
        code_text = "```\nThis is a code block\n```"
        heading1_text = "# Heading 1"
        heading2_text = "## Heading 2"
        heading3_text = "### Heading 3"
        heading4_text = "#### Heading 4"
        heading5_text = "##### Heading 5"
        heading6_text = "###### Heading 6"
        more_hashtags = "####### Not a heading"
        unordered_list_asterisk = "* Item 1\n* Item 2"
        unordered_list_dash = "- Item 2\n- Item2"
        quote_text = "> This is a quote"
        ordered_list_text = "1. Item 1\n2. Item 2"
        self.assertEqual(block_to_block_type(paragraph_text), "paragraph")
        self.assertEqual(block_to_block_type(code_text), "code")
        self.assertEqual(block_to_block_type(heading1_text), "heading")
        self.assertEqual(block_to_block_type(heading2_text), "heading")
        self.assertEqual(block_to_block_type(heading3_text), "heading")
        self.assertEqual(block_to_block_type(heading4_text), "heading")
        self.assertEqual(block_to_block_type(heading5_text), "heading")
        self.assertEqual(block_to_block_type(heading6_text), "heading")
        self.assertNotEqual(more_hashtags, "heading")
        self.assertEqual(block_to_block_type(unordered_list_asterisk), "unordered_list")
        self.assertEqual(block_to_block_type(unordered_list_dash), "unordered_list")
        self.assertEqual(block_to_block_type(quote_text), "quote")
        self.assertEqual(block_to_block_type(ordered_list_text), "ordered_list")


if __name__ == "__main__":
    unittest.main()
