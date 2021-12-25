def sleep_in(weekday, vacation):
    if weekday == False or vacation == True:
        return True
    else:
        return False
        
result = sleep_in(False, False)
print(result)
result = sleep_in(True, False)
print(result)
result = sleep_in(False, True)
print(result)
result = sleep_in(True, True)
print(result)

    