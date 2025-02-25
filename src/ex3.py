def my_maximum_while(lst):
    if not lst:
        return None

    max_val = lst[0]
    max_index = 0
    i = 1

    while i < len(lst):
        if lst[i] > max_val:
            max_val = lst[i]
            max_index = i
        i += 1

    return [max_index, max_val]

print(my_maximum_while([1, 3, 10, 4]))