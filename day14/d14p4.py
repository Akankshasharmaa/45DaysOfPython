def centered_average(arr):
    if len(arr) >= 3:
        new_arr = []
    
        min_num = min(arr)
        max_num = max(arr)

        min_index = arr.index(min_num)
        arr[min_index] = 0

        max_index = arr.index(max_num)
        arr[max_index] = 0

        arr_sum = sum(arr)
        count = len(arr) - 2

        avg_arr = arr_sum // count
        return avg_arr

    return 0

result = centered_average([1, 2, 3, 4, 100])
print(result)
result = centered_average([1, 1, 5, 5, 10, 8, 7])
print(result)
result = centered_average([-10, -4, -2, -4, -2, 0])
print(result)
result = centered_average([7, 7, 7])
print(result)