# Банкомат видає суму дрібними, але не більше 10 штук кожної дрібної купюри
price = int(input("Введите сумму: "))
size = 10
bills = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
total = 0
using_bills = []
for i in bills:
    total += i * size
    using_bills.append(i)
    if total >= price:
        break
if not using_bills:
    print('Сумма не может быть достигнута')
else:
    result = dict.fromkeys(using_bills, 0)
    while price:
        # юзингБилс=[1,2,5]. , берем от последнего элемента
        current_bills = using_bills[-1]
        # 33 - 5 = 28.
        price -= current_bills
        # использовали одну пятерку, добавляем это в слоаврь. и так далее по списку
        result[current_bills] += 1
        if sum(using_bills[:-1]) * size >= price:
            using_bills = using_bills[:-1]
        print(result)

# while amount:
#    current_banknote = using_banknotes[-1]  # берем последний элемент
#    amount -= current_banknote
#    result[current_banknote] += 1
# срезаем список, делая сумму 1 и 2 = 3. и проверяем можем ли мы то что осталось покрыть
# купюрами без последнейю . 28 можно покрыть только 1 и 2 - поэтому на следующей итерации,
# мы опять берем самую большую купюру из используемых - двойку. отнимаем ее до тех пор, пока оставшуюся сумму
# нельзя выдать только единичками.
# if sum(using_banknotes[:len(using_banknotes)-1]) * size >= amount:
#   using_banknotes = using_banknotes[:len(using_banknotes)-1]
# print(result)
