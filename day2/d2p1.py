def pos_neg(a, b, negative):
    if negative == False:
            if (a < 0 and b > 0) or (a > 0 and b < 0):
                return True
            else:
                return False
    elif negative == True and a < 0 and b < 0:
        return True
    else:
        return False



result = pos_neg(4, 5, True)
print("Expected Result = {}, Actual Result = {}".format(False, result))
result = pos_neg(1, -1, True)
print("Expected Result = {}, Actual Result = {}".format(False, result))
result = pos_neg(-1, 1, True)
print("Expected Result = {}, Actual Result = {}".format(False, result))
result = pos_neg(-5, -6, True)
print("Expected Result = {}, Actual Result = {}".format(True, result))
result = pos_neg(4, 5, False)
print("Expected Result = {}, Actual Result = {}".format(False, result))
result = pos_neg(1, -1, False)
print("Expected Result = {}, Actual Result = {}".format(True, result))
result = pos_neg(-1, 1, False)
print("Expected Result = {}, Actual Result = {}".format(True, result))
result = pos_neg(-5, -6, False)
print("Expected Result = {}, Actual Result = {}".format(False, result))
