# https://www.codewars.com/kata/57b58827d2a31c57720012e8/train/python

def fuel_price(litres, price_per_litre):
    price_per_litre = price_per_litre * 100
    for i in range(1, litres + 1):
        if litres >= 10:
            return round(litres * (price_per_litre - 25), 2)/100
        elif litres >= 8:
            return round(litres * (price_per_litre - 20), 2)/100
        elif litres >= 6:
            return round(litres * (price_per_litre - 15), 2)/100
        elif litres >= 4:
            return round(litres * (price_per_litre - 10), 2)/100
        elif litres >= 2:
            return round(litres * (price_per_litre - 5), 2)/100