# if __name__ == '__main__':
#     tests = map(int, input().split()) # this is clear? YES
#     print(f"tests = {tests}")         # This is clear? LAZY

def sq(x):
    return x * x

my_output = list(map(sq, [1, 2, 3, 4]))
print(my_output)