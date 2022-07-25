def sum_of_digits(num):
    res = 0
    if num < 0:
          num = num * -1

    while num > 0:
        sum = num%10
        res += sum
        num = num // 10

    print(res)

num = 123
sum_of_digits(num)
