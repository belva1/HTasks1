def n_low(n):
    return n.lower()

def m_upp(m):
    return m.upper()

l = 'Hi Hello Hi'.split()
print(list(map(n_low, l)))
print(list(map(m_upp, l)))