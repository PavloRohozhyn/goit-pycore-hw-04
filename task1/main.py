""" import Path (work with file), sys modules """
from pathlib import Path
import sys


def total_salary(path: str) -> tuple | Exception:
    """ a function that calculates average and total wages """
    # total of salary
    total_of_salary = 0
    # value for calculating average of salary
    counter = 0
    # create file object
    path = Path(path)
    # check if file exists
    if not path.is_file():
        raise FileNotFoundError('file not found')
    # open file
    with open(path, 'r', encoding='utf-8') as file:
        # read file by line
        for line in file:
            # split content from line
            content = line.split(',')
            # content[0] -> name of employee
            # content[1] -> salary of employee
            result = content[1].strip()
            if result and len(result) > 0:
                total_of_salary += int(content[1])
                counter += 1
            else:
                raise ValueError('wrong or empty data were passed')
    return (total_of_salary,total_of_salary/counter)


# Main
if __name__ == '__main__':
    try:
        # !!!
        # тут багато питань як користувач надасть шлях, в умові сказано:
        # що функція приймає шлях, я вважаю шо шлях з початку є коректним
        total, average = total_salary("/home/cooper/Documents/WOOLF/tier1/Python Programming/homeworks/goit-pycore-hw-04/task1/data")
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

    except (FileNotFoundError, ValueError) as e:
        print(f'Something went wrong, {e}')
        sys.exit(0)
