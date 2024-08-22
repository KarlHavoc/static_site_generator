import unittest

from inline_markdown import (
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes,
)
from textnode import (
    TextNode,
    text_type_bold,
    text_type_code,
    text_type_image,
    text_type_italic,
    text_type_link,
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

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_extract_link(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        links_list = extract_markdown_links(text)
        self.assertEqual(
            links_list,
            [
                ("to boot dev", "https://www.boot.dev"),
                ("to youtube", "https://www.youtube.com/@bootdotdev"),
            ],
        )

    def test_extract_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        image_list = extract_markdown_images(text)
        self.assertEqual(
            image_list,
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
            ],
        )

    def test_split_nodes_image(self):
        node = TextNode(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
            text_type_text,
        )
        nodes_list = split_nodes_image([node])
        self.assertEqual(
            nodes_list,
            [
                TextNode("This is text with a ", text_type_text),
                TextNode(
                    "rick roll", text_type_image, "https://i.imgur.com/aKaOqIh.gif"
                ),
                TextNode(" and ", text_type_text),
                TextNode(
                    "obi wan", text_type_image, "https://i.imgur.com/fJRm4Vk.jpeg"
                ),
            ],
        )

    def test_split_nodes_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            text_type_text,
        )
        new_nodes = split_nodes_link([node])
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a link ", text_type_text),
                TextNode("to boot dev", text_type_link, "https://www.boot.dev"),
                TextNode(" and ", text_type_text),
                TextNode(
                    "to youtube", text_type_link, "https://www.youtube.com/@bootdotdev"
                ),
            ],
        )

    def test_no_link_or_image(self):
        node = TextNode(
            "This is text with a link to boot dev https://www.boot.dev and to youtube https://www.youtube.com/@bootdotdev",
            text_type_text,
        )
        new_nodes_image = split_nodes_image([node])
        new_nodes_link = split_nodes_link([node])
        self.assertEqual([node], new_nodes_image)
        self.assertEqual([node], new_nodes_link)

    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertEqual(
            nodes,
            [
                TextNode("This is ", text_type_text),
                TextNode("text", text_type_bold),
                TextNode(" with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word and a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" and an ", text_type_text),
                TextNode(
                    "obi wan image", text_type_image, "https://i.imgur.com/fJRm4Vk.jpeg"
                ),
                TextNode(" and a ", text_type_text),
                TextNode("link", text_type_link, "https://boot.dev"),
            ],
        )
