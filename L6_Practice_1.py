# https://www.codewars.com/kata/55edaba99da3a9c84000003b/train/python
def divisible_by(numbers, divisor):
    n = []
    for i in numbers:
        if not i % divisor:
            n.append(i)
    return n