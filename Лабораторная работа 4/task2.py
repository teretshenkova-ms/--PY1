default_num = 0  # кол-во букв в строке по умолчанию


def get_count_char(str_):  # функция считает частоту каждой буквы в строке
    dict_count = {}  # пустой шаблон словаря

    for letter in str_.lower():  # перебор без учета регистра
        if letter.isalpha():  # проверка, что символ - буква
            dict_count[letter] = dict_count.get(letter, default_num) + 1  # заполнение словаря
    return dict_count


def get_percent_char(dict_):  # функция меняет частоту букв в словаре на процент от общего кол-ва
    dict_percent = {}  # пустой шаблон словаря
    for char_ in dict_:
        percent = round(my_dict.get(char_) / sum(my_dict.values()) * 100, 1)  # пересчет процента
        dict_percent[char_] = percent  # заполнение словаря
    return dict_percent

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

my_dict = get_count_char(main_str)  # словарь с частотой встречи букв в строке
print(my_dict)
#print(round(sum(get_percent_char(my_dict).values()), 1))  # проверка, что сумма процентов всех букв = 100
