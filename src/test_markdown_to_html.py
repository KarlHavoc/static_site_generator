import unittest

from markdown_to_html import (
    heading_to_html_node,
    markdown_to_html_node,
    paragraph_to_html_node,
    quote_to_html_node,
    text_to_children,
)

block_text_paragraph = "This is a paragraph"
block_text_bold = "This is text **with** bold text"
block_text_list = "* Item 1\n* Item 2\n* Item 3"
block_text_code = """
```
This is a code block
```
"""

md_text = """## This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""


class TestMarkdownToHtml(unittest.TestCase):

    def test_text_to_children(self):
        children = text_to_children(block_text_bold)
        self.assertEqual(children[0].tag, None)
        self.assertEqual(children[0].value, "This is text ")
        self.assertEqual(children[1].tag, "b")
        self.assertEqual(children[1].value, "with")
        self.assertEqual(children[2].tag, None)
        self.assertEqual(children[2].value, " bold text")

    def test_paragraph_to_htmlnode(self):
        block = "This is a paragraph of text. It has some **bold** and *italic* words inside of it."
        node = paragraph_to_html_node(block)
        self.assertEqual(
            node.to_html(),
            "<p>This is a paragraph of text. It has some <b>bold</b> and <i>italic</i> words inside of it.</p>",
        )

    # def test_code_to_htmlnode(self):
    #     block = block_text_code
    #     node = code_to_html_node(block)
    #     self.assertEqual(node.to_html(), "<pre><code>This is a code block</code></pre>")

    def test_heading_to_htmlnode(self):
        block = "## This is a heading"
        node = heading_to_html_node(block)
        self.assertEqual(node.to_html(), "<h2>This is a heading</h2>")

    def test_quote_to_htmlnode(self):
        block = "> This is a quote block"
        node = quote_to_html_node(block)
        self.assertEqual(
            node.to_html(), "<blockquote>This is a quote block</blockquote>"
        )

    def test_codeblock(self):
        md = """
```
This is a code block
```

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is a code block\n</code></pre><p>this is paragraph text</p></div>",
        )
