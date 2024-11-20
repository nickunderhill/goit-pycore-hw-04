"""
This module provides functionality to read and process information about cats from a file.

The main function provided is `get_cats_info`, which reads a file containing cat information
and returns a list of dictionaries with each cat's details.
"""

from typing import List, Dict, Union

def get_cats_info(path: str) -> List[Dict[str, Union[str, int]]]:
    """
    Reads a file containing information about cats and returns a list of dictionaries.

    The file should contain lines in the format: cat_id,name,age.

    Parameters:
    path (str): The path to the file containing cats' information.

    Returns:
    List[Dict[str, Union[str, int]]]: A list of dictionaries, where each dictionary represents
    a cat with its id, name, and age.

    Raises:
    FileNotFoundError: If the file is not found.
    ValueError: If there is an issue with the data format.
    """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            cats = []
            for line in lines:
                cat_id, name, age = line.split(',')
                cats.append({
                    'id': cat_id.strip(),
                    'name': name.strip(),
                    'age': int(age.strip())
                })
    except FileNotFoundError as exc:
        raise FileNotFoundError('File not found') from exc
    except ValueError as exc:
        raise ValueError('Invalid data format') from exc

    return cats

if __name__ == '__main__':
    print('Normal file:')
    try:
        cats_info = get_cats_info('task02/cats_normal.txt')
        print(cats_info)
    except (FileNotFoundError, ValueError) as e:
        print(e)
    print()

    print('Empty file:')
    try:
        cats_info = get_cats_info('task02/cats_empty.txt')
        print(cats_info)
    except (FileNotFoundError, ValueError) as e:
        print(e)
    print()

    print('No file:')
    try:
        cats_info = get_cats_info('task02/cats_no_file.txt')
        print(cats_info)
    except (FileNotFoundError, ValueError) as e:
        print(e)
    print()
