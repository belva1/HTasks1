# https://www.codewars.com/kata/56453a12fcee9a6c4700009c/train/python
def close_compare(a, b, margin = 0):
    if margin >= abs(a - b):
        return 0
    else:
        if a < b:
            return -1
        else:
            return 1