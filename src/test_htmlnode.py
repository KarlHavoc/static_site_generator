import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):

    def test_props_to_html(self):
        node = HTMLNode(
            props={
                "href": "https://www.google.com",
                "target": "node",
            }
        )

        self.assertEqual(
            node.props_to_html(), " href=https://www.google.com target=node"
        )

    def test_value(self):
        node = HTMLNode(
            tag="p",
            value="Text goes here",
            children=None,
            props={
                "href": "https://www.google.com",
                "target": "node",
            },
        )
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Text goes here")
        self.assertEqual(node.children, None)
        self.assertEqual(
            node.props,
            {
                "href": "https://www.google.com",
                "target": "node",
            },
        )

    def test_repr(self):
        node = HTMLNode(
            tag="p",
            value="Text goes here",
            children=None,
            props={
                "href": "https://www.google.com",
                "target": "node",
            },
        )
        self.assertEqual(
            "HTMLNode(p, Text goes here, None, {'href': 'https://www.google.com', 'target': 'node'})",
            repr(node),
        )
