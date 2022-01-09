def ascii_code(name):
    # output = []
    # for item in name:
    #     output.append(ord(item))
    # return output

    output = [ord(item) for item in name]
    return output

result = ascii_code('IronMan')
print(result)

