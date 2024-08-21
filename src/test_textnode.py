import unittest

from textnode import TextNode, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a node.", "bold")
        node2 = TextNode("This is a node.", "bold")
        self.assertEqual(node, node2)

    def test_text_eq(self):
        node = TextNode("This is a not a node.", "bold")
        node2 = TextNode("This is a node.", "bold")
        self.assertNotEqual(node, node2)

    def test_text_type_eq(self):
        node = TextNode("This is a node.", "italic")
        node2 = TextNode("This is a node.", "bold")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a node.", "bold", "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a node., bold, https://www.boot.dev)", repr(node)
        )

    def test_text_node_to_html_bold(self):
        t_node = TextNode("text here", "bold", None)
        html_node = text_node_to_html_node(t_node)
        self.assertEqual(html_node.__repr__(), "LeafNode(b, text here, None)")

    def test_text_node_to_html_link(self):
        t_node = TextNode("click here", "link", "https://www.boot.dev")
        html_node = text_node_to_html_node(t_node)
        self.assertEqual(
            html_node.__repr__(),
            "LeafNode(a, click here, {'href': 'https://www.boot.dev'})",
        )


if __name__ == "__main__":
    unittest.main()
