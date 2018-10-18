import os
import shutil


def main():
    demo_walk()


def get_file_type(file_name):
    file_type = ""
    marker = ""
    for character in file_name:
        if character == ".":
            if marker == ".":
                file_type = ""
            marker = character
            continue
        if marker == ".":
            file_type += character
    return file_type


def move_file(file_name, folder_name):
    try:
        os.mkdir(folder_name)
    except FileExistsError:
        pass
    shutil.move(file_name, folder_name + "/" + file_name)


def demo_walk():
    """Process all subdirectories using os.walk()."""
    sort_dict = {}
    os.chdir('FilesToSort')
    for directory_name, subdirectories, file_names in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", file_names)
        print("(Current working directory is: {})".format(os.getcwd()))
        for file_name in file_names:
            file_name = os.path.join(directory_name, file_name)
            file_type = get_file_type(file_name)
            if file_type in sort_dict:
                move_file(file_name, sort_dict[file_type])
            else:
                print("File type is: {}. Store in which folder?".format(file_type))
                folder_name = input(">>> ")
                sort_dict[file_type] = folder_name
                move_file(file_name, sort_dict[file_type])


main()
