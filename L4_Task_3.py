# https://www.codewars.com/kata/5bb904724c47249b10000131/train/python From lesson

def points(games):
    result = 0
    for score in games:
        x, y = score.split(":")
        x, y = int(x), int(y)

        if x > y:
            result += 3
        elif x == y:
            result += 1
    return result