a = 'abc'
b = (10, 20, 30)

def min_range(a,b):
      return range(len(sorted((a,b), key=len)[0]))

c = ((a[i], b[i])
         for i in min_range(a,b))

for i in c:
    print(i)