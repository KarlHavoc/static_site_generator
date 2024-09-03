import os
from pathlib import Path

from extract_markdown import extract_title
from markdown_to_html import markdown_to_html_node


def generate_page(from_path, template_path, dest_path):
    print(f" * {from_path} {template_path} -> {dest_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)


def generate_page_recursive(dir_path_content, template_path, dest_dir_path):
    filenames = os.listdir(dir_path_content)
    for filename in filenames:
        filename = Path(filename)
        content_path = os.path.join(dir_path_content, filename)
        if filename.suffix == ".md":
            html_filename = filename.with_suffix(".html")
            dest_path = os.path.join(dest_dir_path, html_filename)
        else:
            dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(content_path):
            # content_path = Path(content_path)
            # html_content_path = content_path.with_suffix(".html")
            # content_path.replace(html_content_path)
            generate_page(content_path, template_path, dest_path)
        else:
            generate_page_recursive(content_path, template_path, dest_path)
