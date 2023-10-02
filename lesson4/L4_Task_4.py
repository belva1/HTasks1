# https://www.codewars.com/kata/5b077ebdaf15be5c7f000077/train/python From lesson
def count_sheep(n):
    result = ""
    word = "sheep..."
    for i in range(1, n+1):
        result += f"{i} {word}"
    return result