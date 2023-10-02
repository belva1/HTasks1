# https://www.codewars.com/kata/559d2284b5bb6799e9000047/train/python

def add_length(str_):
    return list(map(lambda x: " ".join([x, str(len(x))]), str_.split(" ")))

# map - будет применять функцию к каждому итератору из списка
# Задали лямбду, параметр. с помощью джоин сделали разделитель для итерируемого объекта и его длинны
# В конце с помощью сплит разделила строку по разделителю

def add_length(str_):
    answer = []
    for word in str_.split():
        answer.append(word + ' ' + str(len(word)))
    return answer
# Это решение мне больше нравится (оно из списка решений)