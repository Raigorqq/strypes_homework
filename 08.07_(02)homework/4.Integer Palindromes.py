def is_int_palindrome(n):
    sum = n
    res = 0
    while(n>0):
        a = n % 10
        res = res * 10 + a
        n = n // 10
    if(sum == res):
        print("True")
    else:
        print("False")

n = 212
is_int_palindrome(n)
