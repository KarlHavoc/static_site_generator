from block_markdown import block_to_block_type, markdown_to_blocks
from htmlnode import LeafNode, ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node

block_type_heading = "heading"
block_type_paragraph = "paragraph"
block_type_code = "code"
block_type_quote = "quote"
block_type_ol = "ordered_list"
block_type_ul = "unordered_list"


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)


def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == block_type_paragraph:
        return paragraph_to_html_node(block)
    if block_type == block_type_heading:
        return heading_to_html_node(block)
    if block_type == block_type_code:
        return code_to_html_node(block)
    if block_type == block_type_ol:
        return ol_to_html_node(block)
    if block_type == block_type_ul:
        return ul_to_html_node(block)
    if block_type == block_type_quote:
        return quote_to_html_node(block)
    raise ValueError("Invalid block type")


def text_to_children(text):
    child_node_list = []
    text_nodes = text_to_textnodes(text)
    for node in text_nodes:
        child_node_list.append(text_node_to_html_node(node))

    return child_node_list


def paragraph_to_html_node(block):
    lines = block.split("\n")
    text = " ".join(lines)
    children = text_to_children(text)
    return ParentNode("p", children)


def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])


def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"Invalid heading level: {level}")
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)


def quote_to_html_node(block):
    text = block[2:]
    children = text_to_children(text)
    return ParentNode("blockquote", children)


def ol_to_html_node(block):
    children = []
    lines = block.split("\n")
    for line in lines:
        line_text = line[3:]
        children.append(LeafNode("li", line_text))
    return ParentNode(block_type_ol, children)


def ul_to_html_node(block):
    children = []
    lines = block.split("\n")
    for line in lines:
        line_text = line[2:]
        children.append(LeafNode("li", line_text))
    return ParentNode(block_type_ul, children)
