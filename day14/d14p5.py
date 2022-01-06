def sum13(arr):
    if len(arr) >= 1:
        for num in arr:
            if num == 13:
                index_13 = arr.index(13)
                arr[index_13] = 0
            
                if  len(arr) - 1 != index_13:
                    arr[index_13+1] = 0
        mysum = sum(arr)
        return mysum
    else:
        return 0

result = sum13([1, 2, 2, 1])
print(result)
result = sum13([1, 1])
print(result)
result = sum13([1, 2, 2, 1, 13])
print(result)