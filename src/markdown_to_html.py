from block_markdown import block_to_block_type, markdown_to_blocks
from htmlnode import HTMLNode, LeafNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node

block_type_heading = ("heading",)
block_type_paragraph = ("paragraph",)
block_type_code = ("code",)
block_type_quote = ("quote",)
block_type_ol = ("ordered_list",)
block_type_ul = ("unordered_list",)


def markdown_to_htmlnode(markdown):
    # markdown to blocks returns a list of blocks
    blocks_list = markdown_to_blocks(markdown)
    block_nodes_list = []
    # get types of blocks
    for block in blocks_list:
        block_type = block_to_block_type(block)
        html_attributes = block_type_to_html_node_attributes(block_type, block)
        
    pass


# define function that takes ol or ul and returns list of leafnodes with proper tags for items in list <li></li>

def list_blocks_to_children(HTMLNode):
    children = []
    lines = HTMLNode.value.split("\n")
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
        html_attributes["tag"] = "code"
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
