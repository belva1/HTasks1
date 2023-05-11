# Example of using "if" with operators not, and

a = int(input("a = "))
b = int(input("b = "))
if a not in range(1, 5) and b not in range(1, 5):
    print("True")
else:
    print("False")

# Task from CodeWars with "If" using
# https://www.codewars.com/kata/5b853229cfde412a470000d0/train/python

def twice_as_old(dad_years_old, son_years_old):
    difference = dad_years_old - son_years_old
    twice_as_old = difference * 2
    if dad_years_old >= twice_as_old:
        return dad_years_old - twice_as_old
    else:
        return twice_as_old - dad_years_old