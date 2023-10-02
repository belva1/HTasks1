# https://www.codewars.com/kata/5631213916d70a0979000066/solutions/python
def pattern(n):
    output_str = ''
    for elem in range(1, n + 1):
        if elem == 1:
            output_str += f'{elem}'
        else:
            star = '*'
            star *= (elem - 1)
            output_str += f'1{star}{elem}'
            # newline only after all lines except the last one
        if elem != n:
            output_str += '\n'
    return output_str


print(pattern(10))




