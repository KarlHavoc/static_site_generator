import os
import shutil


def main():
    public_path = "/Users/michaelkowalsky/workspace/github.com/KarlHavoc/static_site_generator/public"
    static_path = "/Users/michaelkowalsky/workspace/github.com/KarlHavoc/static_site_generator/static"

    shutil.rmtree(public_path)
    os.mkdir(public_path)
    directories = os.listdir(static_path)
    copy_static_to_public(directories, static_path, public_path)
    # need to make function that takes a file path and recurses and copies everything from file_path to public directory


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


main()
