#!/usr/bin/env python
"""
delete.py
A safer alternative to the rm command
This script provides a wrapper around rm that:
- keeps access to most of it capabilities
- reduces argument bloat
- warns before commiting dangerous operations
- and improves user ergonomics
"""

# Spacemacs: Use SPC SPC python-black-buffer to format

import os
import sys

# terminal colors
# this assigns ANSI color codes to the colors class


class color:
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    DARKCYAN = "\033[36m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"


# detect OS
# if OS is not Unix-based, warn user
if sys.platform == "win32":
    print("Dear Windows user, this script is not guaranteed to work on your operating system.")
    print(color.RED + "Proceed with caution!\n" + color.END)



def main():
    """
    Here is where the main application logic lies
    """
    # Show correct usage if the user provides no arguments and results in error
    if len(sys.argv) == 1:
        print(
            color.BOLD
            + color.RED
            + "  Oops! You didn't provide the filename as an argument!"
            + color.END
        )
        print(color.BOLD + "  THIS is how you use delete.py correctly\n" + color.END)
        print(color.GREEN + "	  ./delete.py" + color.END + " <your-file-or-folder>\n")
        print(color.BOLD + color.YELLOW + "  NOT like this:\n" + color.END)
        print(color.RED + "	  ./delete.py" + color.END)
        print("	  ^ (no arguments)")
        exit()

    # Create variable for file/folder to be deleted
    deleted_file = ""

    # Sanitize command line options
    """
    This switches to the second argument if the first contains an invalid argument.
    This is because, if this script is aliased as "rm" by a user, the script will believe that the argument (e.g. -rf ) is the file to be deleted.
    To prevent that from happening, we always switch to the second user-provided argument.
    """
    if len(sys.argv) > 2:
        deleted_file += sys.argv[2]
    else:
        deleted_file += sys.argv[1]

    # Check if file exists
    if os.path.isfile(deleted_file) == False:
        print(
            color.BOLD
            + "Sorry, the file you selected does not exist. Please try again."
            + color.END
        )
        exit()

    # Ask user for confirms
    if sys.argv[1] == "-ff":
        print(
            "\033[32mYou seem to want to delete the file/folder\033[0m"
            + " ./"
            + deleted_file
        )
        print(
            "Are you \033[1;31mSURE\033[0m you want to \033[1mPERMANENTLY\033[0m delete this file??? (CTRL C to cancel)"
        )
        answer = input("Enter Y/N to confirm: ")

        if answer == "Y" or answer == "y":
            command = "rm -rf " + deleted_file
            os.system(command)
            print("Chosen file(s) erased permanently from disk.")
        elif answer == "N" or answer == "n":
            command = "mv " + deleted_file + " ~/.local/share/Trash/files"
            os.system(command)
            print("Chosen file(s) moved to Trash instead.")
        elif type(answer) == str:
            command = "mv " + deleted_file + " ~/.local/share/Trash/files"
            os.system(command)
            print("Chosen file(s) moved to Trash instead.")
        else:
            print("Operation cancelled.")
            print("Exiting...")

    else:
        print(
            color.PURPLE
            + "You seem to want to move the file/folder"
            + color.END
            + " ./"
            + color.BOLD
            + deleted_file
            + color.END
            + color.PURPLE
            + " to Trash. Are you sure?"
            + color.END
        )
        answer = input("Enter " + color.RED + "Y/N" + color.END + " to confirm: ")
        if answer == "Y" or answer == "y":
            command = "mv " + deleted_file + " ~/.local/share/Trash/files"
            os.system(command)
            print(color.CYAN + "Chosen file(s) moved to Trash." + color.END)
        else:
            print(color.CYAN + "Chosen file(s) not deleted or trashed." + color.END)


# Run application
if __name__ == "__main__":
    try:
        main()
    # Gracefully exit on pressing CTRL C
    except KeyboardInterrupt:
        print(color.GREEN + color.BOLD + "\nOperation cancelled." + color.END)
        print("Exiting...")
