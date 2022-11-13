from random import randint


def get_unique_list_numbers() -> list[int]:  # TODO написать функцию для получения списка уникальных целых чисел
    list_ = []
    i = 0
    while i < 15:
        rand_element = randint(-10, 10)
        if rand_element not in list_:
            list_ += [rand_element]
            i += 1
    return list_


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
