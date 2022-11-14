from random import randint


def get_unique_list_numbers(length, min_value, max_value) -> list[int]:  # TODO написать функцию для получения списка уникальных целых чисел
    list_ = []
    i = 0
    while i < length:
        rand_element = randint(min_value, max_value)
        if rand_element not in list_:
            list_ += [rand_element]
            i += 1
    return list_


list_unique_numbers = get_unique_list_numbers(15, -10, 10)
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
