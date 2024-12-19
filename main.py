"""
Главный модуль программы
Осуществляет выполнение выбранной из меню задачи, посредством вызова
соответствующей подпрограммы
Перед вызовом запрашивает нужные исходные данные подпрограммы
"""


from lab6.my_library import task6_1, line40


def menu():
    """
    Функция предлагает выбор номера задания и номера лабораторной работы\n
    :param : нет передаваемых параметров
    :return: choice_task - выбранный номер задания
             choice_lab - выбранный номер лабы
    """
    choice_task = int(input('Выберите номер задания в лабораторной работе: '))

    return choice_task

if __name__ == '__main__':
    while True:
        choice = menu()
        print('программа запустилась')


        match choice:

            case 1:

                task6_1('input.txt', 'output.txt')  # Вызов функции с заданными файлами

            case 2:

                input_text = input("Введите текст (для завершения введите точку '.'): ")
                with open('input.txt', 'w', encoding='utf-8') as f:
                    f.write(input_text)

                # Вызываем функцию для обработки файла
                line40('input.txt', 'output.txt')

            case _:
                break

        if input('Продолжить? Да/Нет: ') == 'Нет'.lower(): break

