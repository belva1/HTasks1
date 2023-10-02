# Ввести число, вивести усі його дільники.
s = int(input())
for i in range(1, s+1):
    if not i % 2:
        print(i)