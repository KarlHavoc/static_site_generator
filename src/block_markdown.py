def markdown_to_blocks(markdown):
    split_text = markdown.split("\n\n")
    stripped_list = []
    for text in split_text:
        stripped_text = text.strip()
        stripped_list.append(stripped_text)
    return stripped_list
