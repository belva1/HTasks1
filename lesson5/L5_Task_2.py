def simple(n):
    if n in (1, 2, 3):
        return True

    for i in range(2, int(n**0.5) + 2):
        if not n % i:
            return False

    return True


def sqr(m):
    return m ** 2

l = []
for m in range(1, 50):
    if simple(m):
        l.append(sqr(m))

print(l)
