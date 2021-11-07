def power(list_1: list, list_2: list) -> list:
    list_1 += list_2
    return [element ** 3 for element in list(set(list_1))]


print(power([1, 2, 4, 8, 11], [1, 3, 7, 9, 12, 11, 8]))
