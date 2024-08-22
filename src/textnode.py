from htmlnode import LeafNode

text_type_bold = "bold"
text_type_text = "text"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"


class TextNode:

    def __init__(self, text, text_type, url=None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, text_node) -> bool:
        if (
            self.text == text_node.text
            and self.text_type == text_node.text_type
            and self.url == text_node.url
        ):
            return True

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


def text_node_to_html_node(text_node):
    if text_node.text_type == "text":
        new_node = LeafNode(value=text_node.text)
        return new_node
    if text_node.text_type == "bold":
        new_node = LeafNode("b", text_node.text)
        return new_node
    if text_node.text_type == "italic":
        new_node = LeafNode("i", text_node.text)
        return new_node
    if text_node.text_type == "code":
        new_node = LeafNode("code", text_node.text)
        return new_node
    if text_node.text_type == "link":
        new_node = LeafNode("a", text_node.text, {"href": text_node.url})
        return new_node
    if text_node.text_type == "image":
        new_node = LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        return new_node
    else:
        raise Exception(f"Invalid text type: {text_node.text_type}")
