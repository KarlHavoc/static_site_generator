import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):

    def test_props_to_html(self):
        node = HTMLNode(
            props={
                "href": "https://www.google.com",
                "target": "node",
            }
        )

        self.assertEqual(
            node.props_to_html(), ' href="https://www.google.com" target="node"'
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

    def test_LeafNode_no_tag(self):
        leafnode = LeafNode(tag=None, value="NO TAG", props=None)
        self.assertEqual(leafnode.tag, None)

    def test_LeafNode_no_value(self):
        leafnode = LeafNode(tag="a", value=None, props=None)
        self.assertEqual(leafnode.value, None)

    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello World")
        self.assertEqual(node.to_html(), "<p>Hello World</p>")

    def test_LeafNode_to_html(self):
        node = LeafNode("a", "Click here", {"href": "https://www.boot.dev"})
        print(node.__repr__())
        self.assertEqual(
            node.to_html(), '<a href="https://www.boot.dev">Click here</a>'
        )

    def test_ParentNode_no_tag(self):
        child_node = LeafNode("a", "Click here", {"href": "https://www.boot.dev"})
        node = ParentNode(children=child_node)
        self.assertEqual(node.tag, None)

    def test_ParentNode_to_html(self):
        child_node1 = LeafNode("b", "Bold text")
        child_node2 = LeafNode(None, "Normal text")
        child_node3 = LeafNode("i", "italic text")
        node = ParentNode("p", [child_node1, child_node2, child_node3])
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i></p>",
        )

    def test_ParentNode_values(self):
        child_node1 = LeafNode("b", "Bold text")
        node = ParentNode("p", child_node1, None)
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.children, child_node1)
        self.assertEqual(node.props, None)

    def test_ParentNode_multiple_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_parentnode_no_children(self):
        node = ParentNode("p", None)
        self.assertEqual(node.children, None)
