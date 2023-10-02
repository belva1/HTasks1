# Банкомат видає суму максимально можливими купюрами

price = int(input("Введите сумму: "))

bills = [1000, 500, 200, 100, 50, 20, 10]

for i in bills:
    if price // i:
        print(f"Купюр по {i}: {price // i}")
        price %= i
    if not price:
        break