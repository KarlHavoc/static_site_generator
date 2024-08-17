import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a node.", "bold")
        node2 = TextNode("This is a node.", "bold")
        self.assertEqual(node, node2)

    def test_text_eq(self):
        node = TextNode("This is a not a node.", "bold")
        node2 = TextNode("This is a node.", "bold")
        self.assertNotEqual(node, node2)

    def test_text_type(self):
        node = TextNode("This is a node.", "italic")
        node2 = TextNode("This is a node.", "bold")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
