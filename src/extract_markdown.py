def extract_title(markdown):
    lines = markdown.split("\n")
    if not lines[0].startswith("# "):
        raise Exception("Not a valid heading")
    stripped_line = lines[0].lstrip("# ").rstrip(" ")
    return stripped_line
