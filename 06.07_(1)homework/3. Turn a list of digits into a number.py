
from string import digits


def to_number(digits):
    for i in digits:
        print(i, end="")

digits = [1,2,3, 10, 200, 99, 23]
to_number(digits)
