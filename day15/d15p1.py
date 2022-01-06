def sum67(arr):
    if len(arr) >= 1:
        mysum = 0
        adding_allowed = True
        for index, num in enumerate(arr):
            if num == 6:
                adding_allowed = False
            
            if adding_allowed is True:
                mysum += num

            if num == 7:
                adding_allowed = True
        return mysum
    else:
        return 0

result = sum67([1, 2, 2])
print(result)
result = sum67([1, 2, 2, 6, 99, 99, 7])
print(result)
result = sum67([1, 1, 6, 7, 2])
print(result)