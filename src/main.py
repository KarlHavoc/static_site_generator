import os
import shutil

from extract_markdown import extract_title
from markdown_to_html import markdown_to_htmlnode


def main():
    public_path = "/Users/michaelkowalsky/workspace/github.com/KarlHavoc/static_site_generator/public"
    static_path = "/Users/michaelkowalsky/workspace/github.com/KarlHavoc/static_site_generator/static"

    shutil.rmtree(public_path)
    os.mkdir(public_path)
    directories = os.listdir(static_path)
    copy_static_to_public(directories, static_path, public_path)
    generate_page(
        "/Users/michaelkowalsky/workspace/github.com/KarlHavoc/static_site_generator/content/index.md",
        "/Users/michaelkowalsky/workspace/github.com/KarlHavoc/static_site_generator/template.html",
        "/Users/michaelkowalsky/workspace/github.com/KarlHavoc/static_site_generator/public/index.html",
    )


def copy_static_to_public(directories, file_path_to_copy, destination_file_path):
    # public_path = "/Users/michaelkowalsky/workspace/github.com/KarlHavoc/static_site_generator/public"
    # static_path = "/Users/michaelkowalsky/workspace/github.com/KarlHavoc/static_site_generator/static"

    # if len(directories) > 0:
    #     for dir in directories:
    #         new_path = os.path.join(static_path, dir)
    #         print(f"{new_path} This is the new path")
    #         if os.path.isfile(new_path):
    #             shutil.copy(new_path, public_path)
    #         else:
    #             if os.path.exists(new_path):
    #                 directories = os.listdir(new_path)
    #                 print(f"These are the new directories {directories}")
    #                 copy_static_to_public(directories)
    for dir in directories:

        new_path = os.path.join(file_path_to_copy, dir)
        print(f"this is the new path {new_path}")
        if os.path.isfile(new_path):
            print(f"this is a file {new_path}")
            shutil.copy(new_path, destination_file_path)
        else:
            new_destination_path = destination_file_path + "/" + dir
            os.mkdir(new_destination_path)
            directories = os.listdir(new_path)
            copy_static_to_public(directories, new_path, new_destination_path)


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as md_file:
        markdown_text = md_file.read()
    with open(template_path, "r") as html_file:
        html_text = html_file.read()

    htmlnode = markdown_to_htmlnode(markdown_text)
    node_to_html = htmlnode.to_html()
    title = extract_title(markdown_text)
    html_text.replace("{{ Title }}", title)
    html_text.replace("{{ Content }}", node_to_html)
    if not os.path.dirname(dest_path):
        os.makedirs(dest_path)
    with open(dest_path, "w") as file:
        file.write(html_text)


main()
