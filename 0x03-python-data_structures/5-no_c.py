#!/usr/bin/python3
def no_c(my_string):
    str_list = list(my_string)
    idx_count = 0
    for idx in str_list:
        if idx == 'c' or idx == 'C':
            str_list[idx_count] = ""
        idx_count += 1
    return "".join(str_list)
