import unittest

from inline_markdown import split_nodes_delimiter
from textnode import (
    TextNode,
    text_type_bold,
    text_type_code,
    text_type_italic,
    text_type_text,
)


class TestSplitDelimiter(unittest.TestCase):

    def test_split_delimiter_code(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" word", text_type_text),
            ],
        )

    def test_split_delimiter_bold(self):
        node = TextNode("This is text with a **bold** word", text_type_text)
        new_node = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertEqual(
            new_node,
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bold", text_type_bold),
                TextNode(" word", text_type_text),
            ],
        )

    def test_split_delimiter_double_bold(self):
        node = TextNode("This is **text** with a **bold** word", text_type_text)
        new_node = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertEqual(
            new_node,
            [
                TextNode("This is ", text_type_text),
                TextNode("text", text_type_bold),
                TextNode(" with a ", text_type_text),
                TextNode("bold", text_type_bold),
                TextNode(" word", text_type_text),
            ],
        )

    def test_split_delimiter_italic(self):
        node = TextNode("This is text with an *italic* word", text_type_text)
        new_node = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertEqual(
            new_node,
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word", text_type_text),
            ],
        )
