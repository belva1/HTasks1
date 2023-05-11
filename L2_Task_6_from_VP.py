# https://github.com/PonomaryovVladyslav/PythonCources/blob/master/lesson2.md
age = input('Please enter your age.')
age = int(age)
gender = input("Please enter your gender. Note that only either 'female' or 'male' can be entered.")
name = input('What is your name?')
if 'c' in name or 't' in name:
    print("Sorry, but we don't recommend sports for people with 'c' or 't' in their names.")
elif age < 15:
    print('We recommend tennis lessons to you!')
else:
    if gender == 'male':
        print('We recommend football lessons to you!')
    elif gender == 'female':
        print('We recommend basketball lessons to you!')
    else:
        print("If you didn't receive a recommendation, you most likely entered your gender incorrectly.")
