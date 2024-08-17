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


def main():
    new_node = TextNode("This is a text node", "bold", url="https://www.boot.dev")
    print(new_node.__repr__())


main()
