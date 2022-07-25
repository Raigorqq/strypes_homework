def sum_of_divisors(arr):
    divisors = [1]
    for i in range(2, arr):
        if (arr % i) == 0:
            divisors.append(i)
    print(sum(divisors))

arr = 1
sum_of_divisors(arr)
