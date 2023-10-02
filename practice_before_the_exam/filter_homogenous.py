# https://www.codewars.com/kata/57ef016a7b45ef647a00002d/solutions/python
def filter_homogenous(arrays):
    result = []
    same_type_lists = []
    different_type_lists = []

    for sub_arr in arrays:
        if not sub_arr:
            continue
        first_item_type = type(sub_arr[0])
        all_same_type = True

        for item in sub_arr:
            if type(item) != first_item_type:
                all_same_type = False
                break
        result.append(all_same_type)

        if all_same_type:
            same_type_lists.append(sub_arr)
        else:
            different_type_lists.append(sub_arr)
    return same_type_lists


print(filter_homogenous([[], [1, 2, 3], [], [4, 5, 6], ['a', 'b', 'c'], ['a', 4, 'c']]))

# my_str = 'Hello World'
# if type(my_str) == str:
#     print('THIS IS STR')





