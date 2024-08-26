import unittest

from htmlnode import LeafNode, ParentNode
from markdown_to_html import (
    block_type_paragraph,
    block_type_to_html_node_attributes,
    markdown_to_htmlnode,
    text_to_children,
)

block_text_paragraph = "This is a paragraph"
block_text_bold = "This is text **with** bold text"


class TestMarkdownToHtml(unittest.TestCase):

    def test_block_type_to_htmlnode_attributes(self):
        htmlnode_attributes = block_type_to_html_node_attributes(
            block_type_paragraph, block_text_paragraph
        )
        self.assertEqual(htmlnode_attributes["tag"], "p")
        self.assertEqual(htmlnode_attributes["value"], "This is a paragraph")

    def test_text_to_children(self):
        children = text_to_children(block_text_bold)
        self.assertEqual(children[0].value, "This is text ")
        self.assertEqual(children[1].tag, "b")
        self.assertEqual(children[1].value, "with")
        self.assertEqual(children[2].tag, None)
        self.assertEqual(children[2].value, " bold text")

    def test_markdown_to_htmlnode(self):
        parent_node = markdown_to_htmlnode(block_text_bold)
        self.assertEqual(
            parent_node,
            ParentNode(
                "div",
                [
                    LeafNode(None, "This is text "),
                    LeafNode("b", "with"),
                    LeafNode(None, " bold text"),
                ],
            ),
        )
