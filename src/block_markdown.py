import re

block_type_heading = "heading"
block_type_paragraph = "paragraph"
block_type_code = "code"
block_type_quote = "quote"
block_type_ol = "ordered_list"
block_type_ul = "unordered_list"


def markdown_to_blocks(markdown):
    split_text = markdown.split("\n\n")
    stripped_list = []
    for text in split_text:
        stripped_text = text.strip()
        if stripped_text != "":
            stripped_list.append(stripped_text)
    return stripped_list


# def block_to_block_type(block):
#     if block[:3] == "```" and block[-3:] == "```":
#         return "code"
#     elif block[:2] == "* " or block[:2] == "- ":
#         return "unordered_list"
#     elif block[:1] == ">":
#         return "quote"
#     elif block[:3] == "1. ":
#         return "ordered_list"
#     elif re.match("#{1,6} ", block) is not None:
#         return "heading"
#     else:
#         return "paragraph"
def block_to_block_type(block):
    lines = block.split("\n")

    if re.match("#{1,6} ", block) is not None:
        return block_type_heading
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return block_type_code
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return block_type_paragraph
        return block_type_ul
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return block_type_paragraph
        return block_type_ul
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return block_type_paragraph
            i += 1
        return block_type_ol
    else:
        return block_type_paragraph
