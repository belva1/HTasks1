def spam(number):
    return 'bulochka' * number


def my_sum(list_of_numbers):
    suma = 0
    for i in list_of_numbers:
        suma += i
    return suma


def shortener(s):
    return " ".join(map(lambda i: i if len(i) <= 6 else i[:6] + "*", s.split()))


def compare_ends(words):
    strings = 0
    for i in words:
        if len(i) >= 2 and i[0] == i[-1]:
            strings += 1
    return strings