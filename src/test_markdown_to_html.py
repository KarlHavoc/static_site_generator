import unittest

from htmlnode import HTMLNode
from markdown_to_html import (
    block_type_paragraph,
    block_type_to_html_node_attributes,
    code_blocks_to_child,
    get_children_leafnodes,
    list_blocks_to_children,
    markdown_to_htmlnode,
    text_to_children,
)

block_text_paragraph = "This is a paragraph"
block_text_bold = "This is text **with** bold text"
block_text_list = "* Item 1\n* Item 2\n* Item 3"
block_text_code = "```This is a code block```"

md_text = """## This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""


class TestMarkdownToHtml(unittest.TestCase):

    def test_block_type_to_htmlnode_attributes(self):
        htmlnode_attributes = block_type_to_html_node_attributes(
            block_type_paragraph, block_text_paragraph
        )
        self.assertEqual(htmlnode_attributes["tag"], "p")
        self.assertEqual(htmlnode_attributes["value"], "This is a paragraph")

    def test_text_to_children(self):
        children = text_to_children(block_text_bold)
        self.assertEqual(children[0].tag, None)
        self.assertEqual(children[0].value, "This is text ")
        self.assertEqual(children[1].tag, "b")
        self.assertEqual(children[1].value, "with")
        self.assertEqual(children[2].tag, None)
        self.assertEqual(children[2].value, " bold text")

    def test_list_blocks_to_children(self):
        children = list_blocks_to_children(block_text_list)
        self.assertEqual(children[0].tag, "li")
        self.assertEqual(children[0].value, "Item 1")
        self.assertEqual(children[1].tag, "li")
        self.assertEqual(children[1].value, "Item 2")
        self.assertEqual(children[2].tag, "li")
        self.assertEqual(children[2].value, "Item 3")

    def test_code_blocks_to_child(self):
        child = code_blocks_to_child(block_text_code)
        self.assertEqual(child[0].tag, "code")
        self.assertEqual(child[0].value, "This is a code block")

    def test_get_children_leafnodes(self):
        node = HTMLNode("p", block_text_bold)
        children = get_children_leafnodes(node.value, "bold", node)
        self.assertEqual(children[0].tag, None)
        self.assertEqual(children[0].value, "This is text ")
        self.assertEqual(children[1].tag, "b")
        self.assertEqual(children[1].value, "with")
        self.assertEqual(children[2].tag, None)
        self.assertEqual(children[2].value, " bold text")
        list_node = HTMLNode("li", block_text_list)
        children1 = get_children_leafnodes(list_node.value, "unordered_list", list_node)
        self.assertEqual(children1[0].tag, "li")
        self.assertEqual(children1[0].value, "Item 1")
        self.assertEqual(children1[1].tag, "li")
        self.assertEqual(children1[1].value, "Item 2")
        self.assertEqual(children1[2].tag, "li")
        self.assertEqual(children1[2].value, "Item 3")
        code_node = HTMLNode("code", block_text_code)
        children2 = get_children_leafnodes(code_node.value, "pre", code_node)
        self.assertEqual(children2[0].tag, "code"),
        self.assertEqual(children2[0].value, "This is a code block"),

    def test_markdown_to_htmlnode(self):
        main_node = markdown_to_htmlnode(md_text)
        child_list = main_node.children
        self.assertEqual(main_node.tag, "div")
        self.assertEqual(child_list[0].tag, "h2")
        self.assertEqual(child_list[0].value, "## This is a heading")
        self.assertEqual(child_list[1].children[0].tag, None)
        self.assertEqual(
            child_list[1].children[0].value, "This is a paragraph of text. It has some "
        )
