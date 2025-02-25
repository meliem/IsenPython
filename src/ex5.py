def get_odd_reverse(lst):
    return [x for x in lst if x % 2 == 1][::-1]

print(get_odd_reverse([10, 15, 11, 2, 65, 3, 87, 89]))