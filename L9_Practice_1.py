# Перевірити, чи є число не парним, ділиться чи на три і на п'ять одночасно, але так,
# щоб не ділитися на 10.
s = int(input())
if not s % 10:
    print("fail")
elif s % 2 and not s % 3 and not s % 5:
    print("pass")
else:
    print("fail")