f = open("C:/Users/HP/Documents/a-level/integers.txt", 'r')

for line in f:
    fizz, buzz, fizzbuzz = map(int, line.split())
    for i in range(1, fizzbuzz + 1):
        if i % fizz and i % buzz:
            print(i)
        elif not i % fizz and not i % buzz:
            print('FB')
        elif not i % fizz:
            print('F')
        elif not i % buzz:
            print('B')
        else:
            print(fizzbuzz)
