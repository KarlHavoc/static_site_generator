import re


def markdown_to_blocks(markdown):
    split_text = markdown.split("\n\n")
    stripped_list = []
    for text in split_text:
        stripped_text = text.strip()
        stripped_list.append(stripped_text)
    return stripped_list


def block_to_block_type(block):
    if block[:3] == "```" and block[-3:] == "```":
        return "code"
    elif block[:2] == "* " or block[:2] == "- ":
        return "unordered_list"
    elif block[:1] == ">":
        return "quote"
    elif block[:3] == "1. ":
        return "ordered_list"
    elif re.match("#{1,6} ", block) is not None:
        return "heading"
    else:
        return "paragraph"
