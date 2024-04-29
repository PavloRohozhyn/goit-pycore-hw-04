""" import Path (work with file), sys modules """
from pathlib import Path
import sys


def get_cats_info(path: str) -> dict | Exception:
    """ function that creates a dictionary with data """
    result = []
    # create file object
    path = Path(path)
    # check if file exists
    if not path.is_file():
        raise FileNotFoundError('file not found')
    # open file
    with open(path, 'r', encoding='utf-8') as file:
        # read file by line
        for line in file:
            # split file string 
            id,name,age = line.split(',')
            item = {}
            # create list
            item['id'] = id.strip()
            item['name'] = name.strip()
            item['age'] = age.strip()
            # add to dictionary
            result.append(item)
    return result


# Main
if __name__ == '__main__':
    try:

        cats_info = get_cats_info("/home/cooper/Documents/WOOLF/tier1/Python Programming/homeworks/goit-pycore-hw-04/task2/data")
        print(cats_info)

    except (FileNotFoundError, ValueError) as e:
        print(f'Something went wrong, {e}')
        sys.exit(0)
