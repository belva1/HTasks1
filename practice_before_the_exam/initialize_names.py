# https://www.codewars.com/kata/5768a693a3205e1cc100071f/solutions/python
def initialize_names(name):
    l = name.split()
    if not l:
        return 'No name'
    elif len(l) < 2 or len(l) == 2:
        return ' '.join(l)
    else:
        first_name = l[0]
        last_name = l[-1]
        full_name = f'{first_name}'
        if len(l) > 2:
            middle_names = l[1:-1]
            for middle_name in middle_names:
                full_name += f' {middle_name[0]}.'
        full_name += f' {last_name}'
        return full_name


with_two_middle_names = 'Alice Betty Catherine Davis'
print(initialize_names(with_two_middle_names))

# test = 'Jay R F'
# test_list = test.split()
# str_test_list = ' '.join(test_list)
# print(str_test_list)


