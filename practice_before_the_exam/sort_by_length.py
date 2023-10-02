def sort_by_length(arr):
    """
    This flag will be used to check if at least one element exchange has been made
    in the current iteration. If no exchange has been made in the current iteration,
    it means that the list is already sorted and we can complete the sorting process.
    """
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr) - 1):
            if len(arr[i]) > len(arr[i + 1]):
                cur_elem = arr[i]  # value of current elem which bigger than next one
                arr[i] = arr[i + 1]  # assign the current elem the value of the next element
                arr[i + 1] = cur_elem  # and vice versa
                swapped = True
    return arr


a = ["Telescopes", "Glasses", "Eyes", "Monocles"]
print(sort_by_length(a))