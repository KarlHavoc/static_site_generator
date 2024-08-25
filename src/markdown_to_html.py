from block_markdown import block_to_block_type, markdown_to_blocks
from htmlnode import HTMLNode

block_type_heading = ("heading",)
block_type_paragraph = ("paragraph",)
block_type_code = ("code",)
block_type_quote = ("quote",)
block_type_ol = ("ordered_list",)
block_type_ul = ("unordered_list",)


def markdown_to_htmlnode(markdown):
    # markdown to blocks returns a list of blocks
    blocks_list = markdown_to_blocks(markdown)
    # get types of blocks
    for block in blocks_list:
        block_type = block_to_block_type(block)
        if block_type == block_type_paragraph:
            new_node = HTMLNode("p", block)
            pass
        pass
    pass


# function that takes a block_type and returns the block data
# e.g. quote - tag = <blockquote></blockquote>, value = text of quote, props = None


def block_type_to_html_node_attributes(block_type, block_text):
    if block_type == block_type_paragraph:
        html_attributes = {"tag": "p", "value": block_text}
        return html_attributes

    if block_type == block_type_code:
        html_attributes = {"tag": "code", "value": block_text}
        return html_attributes

    if block_type == block_type_heading:
        count = block_text[:6].count("#")
        html_attributes = {"tag": f"h{count}", "value": block_text}
        return html_attributes

    if block_type == block_type_quote:
        html_attributes = {"tag": "blockquote", "value": block_text}
        return html_attributes

    if block_type == block_type_ol:
        html_attributes = {"tag": "ol", "value": block_text}
        return html_attributes

    if block_type == block_type_ul:
        html_attributes = {"tag": "ul", "value": block_text}
        return html_attributes
