f = open("C:/Users/HP/Documents/a-level/integers.txt", 'r')
f_output = open("C:/Users/HP/Documents/a-level/results.txt", 'w')

for line in f:
    fizz, buzz, fizzbuzz = map(int, line.split())
    result = [ ]
    for i in range(1, fizzbuzz + 1):
        if i % fizz and i % buzz:
            result.append(str(i))
        elif not i % fizz and not i % buzz:
            result.append('FB')
        elif not i % fizz:
            result.append('F')
        elif not i % buzz:
            result.append('B')
        else:
            result.append(fizzbuzz)
    f_output.write(' '.join(result) + '\n')
