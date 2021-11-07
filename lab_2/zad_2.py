def numbers_1(list_of_numbers: list) -> list:
    result = []
    for number in list_of_numbers:
        result.append(number * 2)
    return result


def numbers_2(list_of_numbers: list) -> list:
    list_of_numbers = [number * 2 for number in list_of_numbers]
    return list_of_numbers


print(f"Pętla 'for': {numbers_1([1,2,4,8,11])}")
print(f"Lista składana: {numbers_2([1,2,4,8,11])}")
