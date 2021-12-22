def parrot_trouble(talking, hour):
    
    if talking == True:
        if 0 <= hour < 7 or 20 < hour < 23:
            return True
        else:
            return False
    else:
        return False


result = parrot_trouble(True, 6)
print(result)

result = parrot_trouble(True, 7)
print(result)

result = parrot_trouble(False, 6)
print(result)