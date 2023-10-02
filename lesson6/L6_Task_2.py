# Створити структуру даних для студентів з імен та прізвищ, можна випадкових.
# Придумати структуру даних, щоб вказувати, у якій групі навчається студент
# (Групи Python, FrontEnd, FullStack, Java). Студент може навчатися у кількох групах.
# Потім вивести:
# студентів, які навчаються у двох та більше групах
# студентів, які не навчаються на фронтенді
# студентів, які вивчають Python або Java

groups = {
    1: 'Python',
    2: 'FrontEnd',
    3: 'FullStack',
    4: 'Java',
}

students = {
    'Amy Brown': [groups[4], groups[2]],
    'Alice Aglow': [groups[1], groups[2], groups[3], groups[4]],
    'Berry Bob': [groups[1]],
    'Billy Sight': [groups[3]]
}

two_or_more_groups = []
without_FrontEnd = []
with_Python_or_Java = []

for i in students:
    if len(students[i]) >= 2:
        two_or_more_groups.append(i)
    if groups[2] not in students[i]:
        without_FrontEnd.append(i)
    if groups[1] in students[i] or groups[4] in students[i]:
        with_Python_or_Java.append(i)


print('List of students who study in 2< groups:', two_or_more_groups)
print('List of students who do not study in the FrontEnd group:', without_FrontEnd)
print('List of students who study in Python or Java groups:', with_Python_or_Java)
