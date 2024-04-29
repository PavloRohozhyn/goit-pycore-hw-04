""" import Path (work with file), sys modules, colorama (works with colors) """
from pathlib import Path
import sys
from colorama import Fore, Style


def show_structure(path: str) -> None | Exception:
    """ a function that returns the contents of a directory """

    directory = Path(path)
    # check if file exists
    if not directory.is_dir():
        raise FileNotFoundError('file not found')
    # scan dir
    for item in directory.iterdir():
        # reset color style
        print(Style.RESET_ALL)
        # if dir
        if item.is_dir():
            # show name of dir and check if dir has files (recursion)
            print(Fore.YELLOW + item.name)
            show_structure(item.absolute())
        else:
            # show name of file
            print(Fore.BLUE + item.name)
    return True


# Main
if __name__ == '__main__':
    try:

        "/home/cooper/Documents/WOOLF/tier1/Python Programming/homeworks/goit-pycore-hw-04/task3/test"
        aruments = sys.argv()
        show_structure(aruments[0])

    except (FileNotFoundError, ValueError) as e:
        print(f'Something went wrong, {e}')
        sys.exit(0)
