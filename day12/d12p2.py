def make_chocolate(small_given, big_given, goal):
    if (big_given * 5) + small_given < goal:
        return -1

    if goal % 5 > small_given:
        return -1

    # big_given, big_needed, big_used
    big_needed = goal // 5

    big_used = min(big_given, big_needed)

    small_used = goal - (big_used * 5)
    return small_used
   
    
result = make_chocolate(4, 1, 9)
print(result)
result = make_chocolate(4, 1, 10)
print(result)
result = make_chocolate(4, 1, 7)
print(result)