banknotes = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
max_size = 10
amount = int(input('Enter amount:'))
using_banknotes = []
for i in range(1, len(banknotes) + 1):
    if sum(banknotes[:i]) * max_size > amount:
        using_banknotes = banknotes[:i]
        result = dict.fromkeys(using_banknotes, 0)
        while amount:
            current_banknote = using_banknotes[-1]
            amount -= current_banknote
            result[current_banknote] += 1
            if sum(using_banknotes[:len(using_banknotes) - 1]) * max_size >= amount:
                using_banknotes = using_banknotes[:len(using_banknotes) - 1]
        print(result)
        break
