# https://www.youtube.com/watch?v=xYm6o-TrFeg
# https://www.regular-expressions.info/wordboundaries.html
# Модуль регулярных выражений
import re
# Задала пустой словарь
frequency = {}
# Сохранила текстовый файл в виде строковой переменной, привела к нижнему регистру для легкости считывания
f = open('C:/Users/HP/Documents/a-level/OneLastTime.txt', 'r')
text_strings = f.read().lower()
# Регулярное выражение, которое вернет все слова, количество букв в которых лежит в диапазоне
match_pattern = re.findall(r'\b[a-z]{1,15}\b', text_strings)

for word in match_pattern:
    count = frequency.get(word, 0)
    frequency[word] = count + 1

frequency_list = sorted(frequency.keys())
for words in frequency_list:
    print(words, frequency[words])