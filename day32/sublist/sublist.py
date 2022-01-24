"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4 

def find_sublist(list_one, list_two):
    """
    # 1. find matching index in list_two
    # 2. start matching one by one
    # 3. if mismatch found, reset i = 0, cut list_two at [j:]
    # 4. Go to step # 1
    # 5. Repeat until list_two is exhausted.
    """
    if not list_one or not list_two:
        return SUBLIST
    Type = None
    j = 0
    n = len(list_two)
    while j < n:
        try:
            match_index = list_two.index(list_one[0])
        except ValueError:
            Type = UNEQUAL
            break
        else:
            # start matching one by one
            not_equal = False
            p = 0
            q = match_index
            while p < len(list_one):
                if list_one[p] != list_two[q]:
                    not_equal = True
                p += 1
                q += 1
            if not_equal:
                # Cut the list
                list_two = list_two[match_index+1:]
            else:
                # Entire list matches, we are successful!
                Type = SUBLIST
                break
        j += 1
    return Type

def sublist(list_one, list_two):
    Type = ""
    if  list_one == list_two:
        Type = EQUAL
    elif len(list_one) < len(list_two):
        Type = find_sublist(list_one, list_two)
    elif len(list_two) < len(list_one):
        index = 0
        Type = find_sublist(list_two, list_one)
        if Type == SUBLIST:
            Type = SUPERLIST
    else:
        Type = UNEQUAL
    return Type
