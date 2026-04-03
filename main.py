# импортирование функции summa. из модуля (файла) add / функцию summa - АБСОЛЮТНЫЙ ИМПОРТ Импорт модуля целиком
from utils.add import summa

print(summa(1, 2))

# импортирование модуля add, обращаемся к модулю (файлу) add/к функции summa
from utils import add

print(add.summa(5, 8))

# импортирование модуля add, обращаемся к модулю (файлу) add/к функции summa
from utils.add import *

print(summa(7, 12))


def get_same_numbers(list_1: list[int], list_2: list[int]) -> list[int]:
    tmp_list = list()
    for i in list_1:
        if i in list_2:
            tmp_list.append(i)
    return tmp_list


if __name__ == "__main__":
    print(get_same_numbers([1, 2, 3, 4], [3, 4, 5, 6]))


def get_mask_card_number(number_card: [str | int] = -1) -> str:
    if number_card != -1:
        if str(number_card).isdecimal() != False:
            counter = 0
            step = 4
            number_cart_mask = ""
            for i in str(number_card):
                counter += 1
                if 6 < counter < 13:
                    i = "*"
                number_cart_mask += i
                if step == counter != 16:
                    step += 4
                    number_cart_mask += " "
            if counter != 16:
                return "Error_01"  # не верное количесвто символов в номере карты
        else:
            return "Error_02"  # введён не числовой символ в номере карты
    else:
        return "Error_03"  # не введён номер карты
    return number_cart_mask


print(get_mask_card_number("7000792289606361"))


def get_mask_account(number_account: [str | int] = -1) -> str:
    if number_account != -1:
        if str(number_account).isdecimal() != False:
            counter = 0
            step = 4
            number_account_mask = ""
            for i in str(number_account):
                counter += 1
                if 14 < counter < 17:
                    i = "*"
                if counter > 14:
                    number_account_mask += i
                if step == counter != 20:
                    step += 4
                    if 14 < counter:  # исключаем пробелы первых 3-х step
                        number_account_mask += (
                            " "  # при выполненнии добавляем пробел с шагом в 4 символа
                        )
            if counter != 20:
                return "Error_04"  # не верное количесвто символов в номере счёта
        else:
            return "Error_05"  # введён не числовой символ в номере счёта
    else:
        return "Error_06"  # не введён номер счёта
    return number_account_mask


print(get_mask_account("73654108430135874305"))
