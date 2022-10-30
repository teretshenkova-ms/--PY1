default_index = -1


def delete(list_, index=None):  # TODO реализовать функцию удаления элемента из списка по индексу
    if len(list_) > 0:  # проверка, есть ли элементы в списке
        if index is None or index == default_index:  # по умолчанию удаляется последний элемент
            list_ = list_[:default_index]
        elif index >= 0:  # если индекс положительный
            if index < len(list_):  # проверка, что индекс не выходит за границы списка
                list_ = list_[:index] + list_[index+1:]
            else:
                list_ = None
                print("Индекс", index, "находится за границами списка")  # предупреждение
        else:  # если индекс отрицательный
            if abs(index) <= len(list_):  # проверка, что индекс не выходит за границы списка
                list_ = list_[:index] + list_[index+1:]
            else:
                list_ = None
                print("Индекс ", index, "находится за границами списка")
    else:
        list_ = None
        print("Невозможно удалить элемент из пустого списка")

    return list_


print(delete([0, 0, 1, 2], index=0))  # [0, 1, 2]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2, 3]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3, 4]
