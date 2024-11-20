"""
This module provides a function to calculate the total and average salary
from a file containing salary data. The file should have lines in the format: name,salary.
"""

from typing import Tuple

def total_salary(path: str) -> Tuple[int, int]:
    """
    Calculate the total and average salary from a file.

    The file should contain lines in the format: name,salary.
    This function reads the file, calculates the total and average salary,
    and returns them as a tuple (total, average).

    Parameters:
    path (str): The path to the salary file.

    Returns:
    Tuple[int, int]: A tuple containing the total salary and the average salary.

    Raises:
    FileNotFoundError: If the file is not found.
    ValueError: If the file is empty or contains invalid data.
    """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            salary_total = 0
            number = 0
            for line in lines:
                salary_total += int(line.split(',')[1])
                number += 1
    except FileNotFoundError as exc:
        raise FileNotFoundError('File not found') from exc

    if number == 0:
        raise ValueError('Salary file is empty')

    average_salary = int(salary_total / number)
    return (salary_total, average_salary)

if __name__ == '__main__':
    print('Normal file:')
    try:
        total, average = total_salary('task01/salary_normal.txt')
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
    except (FileNotFoundError, ValueError) as e:
        print(e)
    print()


    print('Empty file:')
    try:
        total, average = total_salary('task01/salary_empty.txt')
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
    except (FileNotFoundError, ValueError) as e:
        print(e)
    print()

    print('No file:')
    try:
        total, average = total_salary('task01/salary_no_file.txt')
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
    except (FileNotFoundError, ValueError) as e:
        print(e)
    print()
