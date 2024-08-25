import unittest

from markdown_to_html import block_type_paragraph, block_type_to_html_node_attributes

block_text = "this is a block of code"


class TestMarkdownToHtml(unittest.TestCase):

    def test_markdown_to_htmlnode(self):
        pass

    def test_block_type_to_htmlnode_attributes(self):
        htmlnode_attributes = block_type_to_html_node_attributes(
            block_type_paragraph, block_text
        )
        self.assertEqual(htmlnode_attributes, {"tag": "p", "value": block_text})
