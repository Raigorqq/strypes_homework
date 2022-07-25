def contains_digits(number, digits):
    for i in range(len(digits)):
        new_digits = []
        if str(digits[i]) in str(number):
            new_digits.append(True)
        else:
            new_digits.append(False)
    if False in new_digits:
        print(False)
    else:
        print(True)

number = 6665
digits = [6, 5]
contains_digits(number, digits)
