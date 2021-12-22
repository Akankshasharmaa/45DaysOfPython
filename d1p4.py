def monkey_trouble(a_smile, b_smile):
    if (a_smile == True and b_smile == True) or (a_smile == False and b_smile == False):
        return True
    else:
        return False




we_are_in_treouble = monkey_trouble(True, True)
print(we_are_in_treouble)
we_are_in_treouble = monkey_trouble(False, False)
print(we_are_in_treouble)
we_are_in_treouble = monkey_trouble(True, False)
print(we_are_in_treouble)
