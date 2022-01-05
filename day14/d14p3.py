def big_diff(arr):
    if len(arr) >= 1:
        min_num = min(arr)
        max_num = max(arr)

        difference = max_num - min_num
        return difference
    
    
result = big_diff([10, 3, 5, 6])
print(result)
result = big_diff([7, 2, 10, 9])
print(result)
result = big_diff([2, 10, 7, 2])
print(result)