import os
current_working_directory = os.getcwd()
values = []


def read_file_into_dictionary():
    file = "{}/input.txt".format(current_working_directory)
    data = open(file, 'r')
    lines = data.readlines()
    for line in lines:
        values.append(line.rstrip())


def math_two_digits():
    val1, val2 = find_two_digits()

    print(" VAL 1  : {}".format(val1))
    print(" VAL 2  : {}".format(val2))
    print(" Check  : {} + {} = {}".format(val1, val2, val1+val2))
    print(" Answer : {}\n".format(val1 * val2))


def find_two_digits():
    val1 = val2 = 0
    for one_val in values:
        val1 = int(one_val)
        for two_val in values:
            val2 = int(two_val)
            sum = val1 + val2
            if sum == 2020:
                return val1, val2


def math_three_digits():
    val1, val2, val3 = find_three_digits()

    print(" VAL 1  : {}".format(val1))
    print(" VAL 2  : {}".format(val2))
    print(" VAL 3  : {}".format(val3))
    print(" Check  : {} + {} + {} = {}".format(val1, val2, val3, val1+val2+val3))
    print(" Answer : {}\n".format(val1 * val2 * val3))


def find_three_digits():
    val1 = val2 = val3 = 0
    for one_val in values:
        val1 = int(one_val)
        for two_val in values:
            val2 = int(two_val)
            for three_val in values:
                val3 = int(three_val)
                sum = val1 + val2 + val3
                if sum == 2020:
                    return val1, val2, val3


# Script Entry Point
read_file_into_dictionary()
math_two_digits()
math_three_digits()
