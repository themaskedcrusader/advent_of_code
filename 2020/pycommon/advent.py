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

def read_groups_as_row(cwd, problem_key):
    file = get_full_file_path(cwd, problem_key)
    ret = []
    group_string = ""
    file = open(file, 'r')
    lines = file.readlines()
    for line in lines:
        if line.rstrip() == "":
            ret.append(group_string)
            group_string = ""
            continue
        else:
            group_string = "{} {}".format(group_string, line.rstrip())

    # Capture the last group string and return
    ret.append(group_string)
    return ret
