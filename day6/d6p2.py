def make_out_word(out, word):
    newstr = out[:2] + word + out[2:4]
    return newstr

result = make_out_word('<<>>', 'Yay')
print(result)
result = make_out_word('<<>>', 'WooHoo')
print(result)
result = make_out_word('[[]]', 'word')
print(result)