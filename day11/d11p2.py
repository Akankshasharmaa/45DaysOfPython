def near_ten(num):
    if num >= 0: 
        if num % 10 == 0 or (num+1) % 10 == 0 or (num-1) % 10 == 0 or (num+2) % 10 == 0 or (num-2) % 10 == 0:
            return True
        else:
            return False

result = near_ten(12)
print(result)
result = near_ten(17)
print(result)
result = near_ten(19)
print(result)