from block_markdown import block_to_block_type, markdown_to_blocks
from htmlnode import HTMLNode, LeafNode, ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node

block_type_heading = "heading"
block_type_paragraph = "paragraph"
block_type_code = "pre"
block_type_quote = "quote"
block_type_ol = "ordered_list"
block_type_ul = "unordered_list"


def markdown_to_htmlnode(markdown):
    blocks_list = markdown_to_blocks(markdown)
    block_nodes_list = []
    for block in blocks_list:
        block_type = block_to_block_type(block)
        html_attributes = block_type_to_html_node_attributes(block_type, block)
        new_node = HTMLNode(html_attributes["tag"], html_attributes["value"])
        children = get_children_leafnodes(block, block_type, new_node)
        new_node.children = children
        block_nodes_list.append(new_node)
    main_node = ParentNode("div")
    main_node.children = block_nodes_list
    return main_node
    # 8/26 Just wrote code_blocks_to_child. Need to implement in this function with
    # lists function as well. Next need to write more tests for text_to_children and
    # add to this function. Then make children to html node and then add html node
    # with "div" tag. Write tests


def get_children_leafnodes(block, block_type, htlm_node):
    if block_type == block_type_ol or block_type == block_type_ul:
        children = list_blocks_to_children(block)
        return children
    if block_type == block_type_code:
        child = code_blocks_to_child(block)
        return child
    if block_type == block_type_heading:
        child = heading_block_to_child(block)
        return child
    else:
        children = text_to_children(block)
        return children


def heading_block_to_child(block):
    count = block[:6].count("#")
    block_text = block[count + 1 :]
    child = LeafNode(None, block_text)
    return child


# define function that takes pre tag and returns a child with code tag
def code_blocks_to_child(block):
    block_text = block[3:-3]
    child = [LeafNode("code", block_text)]
    return child


# define function that takes ol or ul and returns list of leafnodes with proper tags for items in list <li></li>


def list_blocks_to_children(block):
    children = []
    lines = block.split("\n")
    for line in lines:
        line_text = line[2:]
        children.append(LeafNode("li", line_text))
    return children


# converts text to list textnodes then converts textnodes to leafnodes
def text_to_children(text):
    child_node_list = []
    text_nodes = text_to_textnodes(text)
    for node in text_nodes:
        child_node_list.append(text_node_to_html_node(node))

    return child_node_list


# function that takes a block_type and returns the block data
# e.g. quote - tag = "quote", value = text of quote, props = None


def block_type_to_html_node_attributes(block_type, block_text):
    html_attributes = {}
    if block_type == block_type_paragraph:
        html_attributes["tag"] = "p"
        html_attributes["value"] = block_text

    if block_type == block_type_code:
        html_attributes["tag"] = "pre"
        html_attributes["value"] = block_text

    if block_type == block_type_heading:
        count = block_text[:6].count("#")

        html_attributes["tag"] = f"h{count}"
        html_attributes["value"] = block_text

    if block_type == block_type_quote:
        html_attributes["tag"] = "blockquote"
        html_attributes["value"] = block_text

    if block_type == block_type_ol:
        html_attributes["tag"] = "ol"
        html_attributes["value"] = block_text

    if block_type == block_type_ul:
        html_attributes["tag"] = "ul"
        html_attributes["value"] = block_text
    return html_attributes
