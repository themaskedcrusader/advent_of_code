import os
current_working_directory = os.getcwd()
values = []


def read_file_into_dictionary():
    file = "{}/input.txt".format(current_working_directory)
    data = open(file, 'r')
    lines = data.readlines()
    for line in lines:
        values.append(line.rstrip())


def trees_encountered_part_2():
    trees = [
        trees_encountered(1, 1),
        trees_encountered(3, 1),
        trees_encountered(5, 1),
        trees_encountered(7, 1),
        trees_encountered(1, 2)
    ]
    product = 1
    for tree in trees:
        product = product * tree

    print("Product of runs: {}".format(product))


def trees_encountered(right, down):
    current = 0
    length = 0
    trees = 0
    count = 0
    for row in values:
        temp = list(row)
        if length == 0:             # Eat first row, continue
            length = len(row) - 1
            count = count + 1
            continue
        current = current + right   # move right
        if current > length:
            current = current - length - 1

        if count % down == 0:       # If we've moved down enough, run the calculation
            if temp[current] == '#':
                trees = trees + 1
        else:
            current = current - right   # we need to move down at least one more row, undo right slope
        count = count + 1

    print("Trees Encountered = {}".format(trees))
    return trees


# Script entry point
read_file_into_dictionary()
# part 1
print(" Part 1 : ")
trees_encountered(3, 1)

print(" Part 2 :")
trees_encountered_part_2()
