# Вам известен номер квартиры, этажность дома и количество квартир на этаже. Задача: написать функцию,
# которая по заданным параметрам напишет, в какой подъезд и на какой этаж подняться, чтобы найти искомую квартиру.

def options(apartment, apartments_in_floor, floors):
# узнаем колличество квартир в подъезде.
    apartments_in_entrance = floors * apartments_in_floor
    print(apartments_in_entrance)
# узнаем в каком подъезде находится квартира путем целого деления квартиры на кол-во квартир в подъезде.
    entrance = apartment // apartments_in_entrance
    entrance += 1
    print(entrance)
# остаток от деления квартиры на кол-во квартир в подъезде нацело делим на кол-во квартир на этаже, чтобы вычислить этаж
    f = apartment % apartments_in_entrance
    print(f)
    floor = f // apartments_in_floor
    print(24 // 3)
    floor += 1
    print(floor)
    return print(entrance, "подъезд,", floor, "этаж,", apartment, "квартира")


options(398, 3, 9)