# https://www.codewars.com/kata/57a5c31ce298a7e6b7000334/train/python

def bin_to_decimal(inp):
    result = 0
    """
    In a binary number, the least significant bit (rightmost) 
    has less weight than the most significant bit (leftmost). 
    When converting double to decimal, we need to start from 
    the least significant bit and gradually move to the next bit. 
    Therefore, to properly set up this process in a loop, 
    it is convenient to start with the least significant bit, 
    which is at the end of the line.
    """
    inp = inp[::-1]

    for i in range(len(inp)):
        digit = int(inp[i])
        result += digit * (2 ** i)
    return result