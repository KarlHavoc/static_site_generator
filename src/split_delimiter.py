from textnode import (
    TextNode,
    text_type_text,
)


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != "text":
            new_nodes.append(node)
        elif delimiter not in node.text:
            raise Exception("Delimiter not found in TextNode text")
        else:
            split_text_list = node.text.split(f"{delimiter}")
            new_nodes.append(TextNode(split_text_list[0], text_type_text))
            new_nodes.append(TextNode(split_text_list[1], text_type))
            new_nodes.append(TextNode(split_text_list[2], text_type_text))
    return new_nodes
