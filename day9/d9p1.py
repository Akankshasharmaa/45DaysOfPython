def combo_string(str1, str2):
    if len(str1) > len(str2):
        newstr = str2 + str1 + str2
        return newstr
    elif len(str2) > len(str1):
        newstr = str1 + str2 + str1
        return newstr
    else:
        return False


result = combo_string('Hello', 'hi')
print(result)
result = combo_string('hi', 'Hello')
print(result)
result = combo_string('aaa', 'b')
print(result)