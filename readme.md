# Advent of Code 2023

Welcome to my solutions for Advent of Code 2023! 

## About Advent of Code

Advent of Code is an annual coding challenge that runs from December 1st to 25th. Each day, a new programming puzzle is released, and participants solve the puzzles to earn stars. It's a great way to learn new languages, practice problem-solving skills, and have fun during the holiday season!

## Solutions

This repository contains my solutions to the Advent of Code 2023 puzzles. Each day's solution is in its own directory, named `day_xx` (e.g., `day_01`, `day_02`).

## Languages

I'm primarily using [list the programming languages you're using] for this year's challenges.

## Structure

Each day's directory contains:

- **README.md:** A brief explanation of the puzzle and my approach to solving it.
- **Solution code:** The code files for solving the puzzle, usually in two parts (part 1 and part 2).
- **Input data:** The input file for the puzzle (if applicable).
- **Output:** The output of my solution for the puzzle (if applicable).

## Notes

- Some solutions might be more optimized or elegant than others. I'm always learning and experimenting with different approaches!
- Feel free to use these solutions as inspiration or learning resources, but please don't copy them directly. The point of Advent of Code is to challenge yourself and learn through problem-solving!

## Happy Coding!

I hope you enjoy my solutions and have a wonderful Advent of Code 2023!

    ```
    import os

    def create_folder_structure():
    base_folder = "AdventOfCode"

    # Create base folder if it doesn't exist
    if not os.path.exists(base_folder):
        os.makedirs(base_folder)

    # Create folders and files for days 1 to 25
    for day in range(1, 26):
        day_folder = os.path.join(base_folder, f"day{day:02}")
        os.makedirs(day_folder, exist_ok=True)

        # Create input.txt file
        input_file_path = os.path.join(day_folder, "input.txt")
        with open(input_file_path, "w") as input_file:
            input_file.write("")

        # Create day01.py file
        day_file_path = os.path.join(day_folder, f"day{day:02}.py")
        with open(day_file_path, "w") as day_file:
            day_file.write("# Day {0:02}\n\n".format(day))
            day_file.write("def solve_part1():\n    pass\n\n")
            day_file.write("def solve_part2():\n    pass\n\n")
            day_file.write("if __name__ == '__main__':\n")
            day_file.write("    print('Part 1:', solve_part1())\n")
            day_file.write("    print('Part 2:', solve_part2())\n")

    if __name__ == "__main__":
    create_folder_structure()
    print("Folder structure created successfully.")

    ```