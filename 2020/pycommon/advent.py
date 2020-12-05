import os


def get_full_file_path(cwd, problem_key):
    return "{}/input/{}.txt".format(cwd, problem_key)


def read_input(cwd, problem_key):
    file = get_full_file_path(cwd, problem_key)
    ret = []
    data = open(file, 'r')
    lines = data.readlines()
    for line in lines:
        ret.append(line.rstrip())
    return ret
