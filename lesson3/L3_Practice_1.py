# Сума списку за допомогою for
a = list(range(10))
b = 0
for i in a:
    b += i
    print(b)

# Сума списку за допомогою while
l = list(range(1, 10))
suma = 0
len_l = len(l)
id_l = 0

while (id_l < len_l):
  suma += l[id_l]
  print(suma)
  id_l += 1
