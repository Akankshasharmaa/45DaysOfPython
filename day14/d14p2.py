def count_evens(arr):
    count = 0
    for num in arr:
        if num%2 == 0:
            count += 1
    return count


result = count_evens([2, 1, 2, 3, 4])
print(result)
result = count_evens([2, 2, 0])
print(result)
result = count_evens([1, 3, 5])
print(result)