""" import Path (work with file), sys modules, colorama (works with colors) """
from pathlib import Path
import sys
from colorama import Fore, Style


def show_structure(path: str, format = '') -> None | Exception:
    """ a function that returns the contents of a directory """

    directory = Path(path)
    # check if file exists
    if not directory.is_dir():
        raise FileNotFoundError('file not found')
    # scan dir
    direc = directory.iterdir()
    direc = sorted(direc)
    for item in direc:

        # if dir
        if item.is_dir():
            # show name of dir and check if dir has files (recursion)
            print(format + Fore.YELLOW + item.name + Style.RESET_ALL)
            format += "|-"
            show_structure(item.absolute(), format)
        else:
            # show name of file
            print(format + Fore.BLUE + item.name + Style.RESET_ALL)
    return True


# Main
if __name__ == '__main__':
    try:

        arguments = sys.argv
        show_structure(arguments[1])

    except (FileNotFoundError, ValueError, IndexError) as e:
        print(f'Something went wrong, {e}')
        sys.exit(0)


# python main.py ./test

#  file01
#  file02
#  file03
#  folder1
#  |-folder2
#  |-|-file21
#  |-|-file22
#  |-|-folder3
#  |-|-|-file31
