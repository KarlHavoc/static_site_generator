import re

from textnode import (
    TextNode,
    text_type_bold,
    text_type_code,
    text_type_image,
    text_type_italic,
    text_type_link,
    text_type_text,
)


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != text_type_text:
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


def extract_markdown_images(text):
    images_list = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return images_list


def extract_markdown_links(text):
    links_list = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return links_list


def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        extracted_image_tuple_list = extract_markdown_images(node.text)
        if len(extracted_image_tuple_list) == 0:
            new_nodes.append(node)
            continue
        for tuple in extracted_image_tuple_list:
            sections = node.text.split(f"![{tuple[0]}]({tuple[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalide markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            new_nodes.append(TextNode(tuple[0], text_type_image, tuple[1]))
            node.text = sections[1]
        if node.text != "":
            new_nodes.append(TextNode(node.text, text_type_text))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        original_text = node.text
        extracted_link_tuple_list = extract_markdown_links(original_text)
        if len(extracted_link_tuple_list) == 0:
            new_nodes.append(node)
            continue
        for tuple in extracted_link_tuple_list:
            sections = original_text.split(f"[{tuple[0]}]({tuple[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            new_nodes.append(TextNode(tuple[0], text_type_link, tuple[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))

    return new_nodes


def text_to_textnodes(text_to_split):
    node = TextNode(text_to_split, text_type_text)
    bold_nodes = split_nodes_delimiter([node], "**", text_type_bold)
    italic_nodes = split_nodes_delimiter(bold_nodes, "*", text_type_italic)
    code_nodes = split_nodes_delimiter(italic_nodes, "`", text_type_code)
    image_nodes = split_nodes_image(code_nodes)
    link_nodes = split_nodes_link(image_nodes)

    return link_nodes
