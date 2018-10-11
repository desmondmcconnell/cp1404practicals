"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import os


def main():
    """Demo os module functions."""
    demo_walk()


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    previous_character = ""
    string = ""
    for character in filename:
        if character.isupper() and previous_character.isalpha():
            string += "_"
        if not previous_character.isalpha():
            if previous_character == "'":
                pass
            else:
                character = character.upper()
        string += character
        previous_character = character
    new_name = string.replace(".TXT", ".txt").replace(" ", "_").replace(".Txt", ".txt")
    return new_name


def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        for filename in filenames:
            filename = os.path.join(directory_name, filename)
            new_name = get_fixed_filename(filename)
            print("Renaming {} to {}".format(filename, new_name))
            os.rename(filename, new_name)


main()
