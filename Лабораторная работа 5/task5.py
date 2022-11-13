from string import digits, ascii_lowercase, ascii_uppercase
from random import sample


def get_random_password() -> str:  # TODO написать функцию генерации случайных паролей
    alphabet = digits + ascii_lowercase + ascii_uppercase
    n = 8  # длина пароля
    return "".join(sample(alphabet, n))


print(get_random_password())
