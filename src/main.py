import os
import shutil

from generate_page import generate_page_recursive


def main():
    public_path = "/Users/michaelkowalsky/workspace/github.com/KarlHavoc/static_site_generator/public"
    static_path = "/Users/michaelkowalsky/workspace/github.com/KarlHavoc/static_site_generator/static"

    shutil.rmtree(public_path)
    os.mkdir(public_path)
    directories = os.listdir(static_path)
    copy_static_to_public(directories, static_path, public_path)
    generate_page_recursive(
        "/Users/michaelkowalsky/workspace/github.com/KarlHavoc/static_site_generator/content",
        "/Users/michaelkowalsky/workspace/github.com/KarlHavoc/static_site_generator/template.html",
        "/Users/michaelkowalsky/workspace/github.com/KarlHavoc/static_site_generator/public",
    )


def copy_static_to_public(directories, file_path_to_copy, destination_file_path):
    for dir in directories:

        new_path = os.path.join(file_path_to_copy, dir)
        if os.path.isfile(new_path):
            shutil.copy(new_path, destination_file_path)
        else:
            new_destination_path = destination_file_path + "/" + dir
            os.mkdir(new_destination_path)
            directories = os.listdir(new_path)
            copy_static_to_public(directories, new_path, new_destination_path)


main()
