"""
This script prints the content of a directory, displaying folders and files with
indentation based on their depth level.
"""


import sys
from pathlib import Path

from colorama import init
from colorama import Fore

init(autoreset=True)

def print_dir_content(directory: str, level: int = 0) -> None:
    """
    Prints the content of a directory with indentation based on the depth level.

    Parameters:
    directory (str): The path to the directory to be printed.
    level (int): The current depth level for indentation. Defaults to 0.

    Returns:
    None
    """

    path = Path(directory)

    if not path.is_dir():
        print(f"The provided path {path} is not a valid directory.")
        return

    indent = ' ' * (level * 4)
    dirs = []
    files = []

    for item in path.iterdir():
        if item.is_dir():
            dirs.append(item)
        else:
            files.append(item)

    for dir_item in dirs:
        print(Fore.LIGHTBLUE_EX + f"{indent}{dir_item.name}/")
        print_dir_content(dir_item, level + 1)

    for file_item in files:
        print(Fore.LIGHTGREEN_EX + f"{indent}{file_item.name}")

if len(sys.argv) > 1:
    path_to_file = sys.argv[1]
    print_dir_content(path_to_file)
else:
    print('Please provide path to file')
