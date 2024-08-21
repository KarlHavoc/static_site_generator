from textnode import (
    TextNode,
    text_type_text,
)


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != "text":
            new_nodes.append(node)
            continue
        split_list = []
        split_text_list = node.text.split(delimiter)
        if len(split_text_list) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(split_text_list)):
            if split_text_list[i] == "":
                continue
            if i % 2 == 0:
                split_list.append(TextNode(split_text_list[i], text_type_text))
            else:
                split_list.append(TextNode(split_text_list[i], text_type))
        new_nodes.extend(split_list)
    return new_nodes
