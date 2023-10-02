fizz = input()
fizz = int(fizz)
buzz = input()
buzz = int(buzz)
fizzbuzz = input()
fizzbuzz = int(fizzbuzz)
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
