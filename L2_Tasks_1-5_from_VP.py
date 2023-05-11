# https://github.com/PonomaryovVladyslav/PythonCources/blob/master/lesson2.md
name = input('What is your name?')
if 'a' not in name.lower(): # name in lower case. As example : input("VaLeRy"), output - valery.
    age = input('Please enter your age.')
    age = int(age)
    if age >= 100:
        print('You did not pass the test because you entered a fake age.') # made up the meaning in the condition print
    elif age >= 18:
        print('You have passed the legal age test.')
    else:
        print('You have failed the legal age test.')
    if age % 2:
        print('Your age is an odd number.')
    else:
        print('Your age is an even number.')
    if 'v' in name.lower() and not age % 2:
        print("You won the prize because you have a V/v in your name and your age is even.")
    else:
        print("You didn't won the prize because you haven't a V/v in your name or your age is odd.")
else:
    print('Sorry, but users with A in their name are not allowed to take the test.')
