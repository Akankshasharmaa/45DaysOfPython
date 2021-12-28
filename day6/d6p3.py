def first_last6(arr):
    if arr[0] == 6 or arr[len(arr)-1] == 6:
        return True
    else: 
        return False

result = first_last6([1, 2, 6])
print(result)
result = first_last6([6, 1, 2, 3])
print(result)
result = first_last6([13, 6, 1, 2, 3])
print(result)