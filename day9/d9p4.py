def cigar_party(num, weekend):
    if weekend == False and 40 <= num <= 60:
        return True
    elif weekend == True and num >= 40:
        return True
    else:
        return False

result = cigar_party(30, False)
print(result)
result = cigar_party(50, False)
print(result)
result = cigar_party(70, True)
print(result)