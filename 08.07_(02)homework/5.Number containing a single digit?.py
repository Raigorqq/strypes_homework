def contains_digit(number, digit):
    if str(digit) in str(number):
        print("True")
    else:
        print("False")

number = 42
digit = 3

contains_digit(number, digit)
