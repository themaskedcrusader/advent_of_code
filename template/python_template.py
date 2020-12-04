#!/usr/bin/python3

import os
import pycommon.advent as advent

problem_key = os.path.basename(__file__).replace(".py", "")


# CODE GOES HERE


def main():
    forest_layout = advent.read_input(os.getcwd(), problem_key)
    trees_encountered(3, 1, forest_layout)
    trees_encountered_part_2(forest_layout)


if __name__ == "__main__":
    main()
