def to_digits(num):
    i = 0
    my_list = []
    while num > 0:
        my_list.insert(i, num%10)
        num = num // 10
        # sum = num%10
        # res += sum
        # num = num // 10
        i += 1
    print(my_list)

num = 325
to_digits(num)
