def same_first_last(arr):
    if len(arr) >= 1 and arr[0] == arr[len(arr)-1]:
        return True
    else:
        return False


result = same_first_last([1, 2, 3])
print(result)
result = same_first_last([1, 2, 3, 1])
print(result)
result = same_first_last([1, 2, 1])
print(result)