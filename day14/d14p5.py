def sum13(arr):
    if len(arr) >= 1:
        if 13 in arr:
            index_13 = arr.index(13)
            my_arr = arr[:index_13]
            mysum = sum(my_arr)
            return mysum
        
        arr_sum = sum(arr)
        return arr_sum
    else:
        return 0

result = sum13([])
print(result)
result = sum13([1, 1])
print(result)
result = sum13([1, 2, 2, 1, 13, 5, 6])
print(result)