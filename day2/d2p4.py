def not_string(mystr):
    first_string = 'not'
    if len(mystr) >= 3:
        if mystr[0] == 'n' and mystr[1] == 'o' and mystr[2] == 't' and mystr[3] == ' ':
            return mystr
        else:
            return first_string + ' ' +mystr
    elif 1 <= len(mystr) <= 3:
        return first_string + ' ' +mystr
    else:
        return mystr

result = not_string('candy')
print(result)
result = not_string('x')
print(result)
result = not_string('not bad')
print(result)
result = not_string('')
print(result)
result = not_string('no')
print(result)