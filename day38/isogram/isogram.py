"""Isogram"""
def is_isogram(string):
    """
    input: string
    return: boolean value
    """
    string = string.lower()
    mystr = []
    already_exists = False
    for i in range(len(string)):
        if string[i] not in mystr:
            already_exists = False
            mystr.append(string[i])
        elif string[i] in mystr:
            if string[i] == "-" or string[i] == " ":
                already_exists = False
                mystr.append(string[i])
            else:
                already_exists = True
                break
    if already_exists == True:
        return False
    return True
