def in1to10(num, outside_mode):
    if outside_mode == False and 1 <= num <= 10:
        return True
    elif outside_mode == True and (num <= 1 or num >= 10):
        return True
    else:
        return False

result = in1to10(5, False)
print(result)
result = in1to10(11, False)
print(result)
result = in1to10(11, True)
print(result)