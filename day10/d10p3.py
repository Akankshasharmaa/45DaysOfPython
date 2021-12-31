def caught_speeding(speed, is_birthday):
    
    if is_birthday == False:
        if speed <= 60:
            ticket = 0   
        elif 61 <= speed <= 80:
            ticket = 1    
        elif speed >= 81:
            ticket = 2
        return ticket

    elif is_birthday == True:
        if speed <= 65:
            ticket = 0  
        elif 66 <= speed <= 85:
            ticket = 1   
        elif speed >= 86:
            ticket = 2
        return ticket

result = caught_speeding(60, False)
print(result)
result = caught_speeding(65, False)
print(result)
result = caught_speeding(65, True)
print(result)