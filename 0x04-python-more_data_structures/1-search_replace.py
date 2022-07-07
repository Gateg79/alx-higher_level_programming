#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def s_r_fine(goat):
        return (goat if goat != search else replace)
    return list(map(s_r_fine, my_list))
