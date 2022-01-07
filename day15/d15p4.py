if __name__ == '__main__':
    n = int(input())
    integer_list = list(map(int, input().split()))

    t =  tuple(integer_list)
    hash_result = hash(t)
    print(hash_result)