import os


def read_input(cwd, problem_key):
    file = "{}/input/{}.txt".format(cwd, problem_key)
    ret = []
    data = open(file, 'r')
    lines = data.readlines()
    for line in lines:
        ret.append(line.rstrip())
    return ret
