def task6_1(input_file, output_file):
    try:
        numbers = []

        while True:
            line = input('Введите целые числа (по одному на строку). Для завершения ввода введите "end": ')  # Чтение строки с клавиатуры
            if line.lower() == 'end':
                break
            # Проверка, является ли строка целым числом (положительным или отрицательным)
            if line.isdigit() or (line[0] == '-' and line[1:].isdigit()):
                # Преобразуем строки в целое число и добавляем в список
                numbers.append(int(line))
            else:
                print("Пожалуйста, введите целое число или 'end' для завершения.")

        # Проверка, не пуст ли список чисел
        if not numbers:
            raise ValueError("Файл пуст или не содержит целых чисел.")

        # Флаг для проверки упорядчены ли числа по возрастанию
        is_sorted = True
        for i in range(len(numbers) - 1):
            if numbers[i] > numbers[i + 1]:
                is_sorted = False
                break

        # Открытие выходного файла для записи
        with open(output_file, 'w', encoding='utf-8') as f:
            if is_sorted:
                # Если числа упорядочены, записываем их в обратном порядке
                for i in range(len(numbers) - 1, -1, -1):
                    f.write(f"{numbers[i]}\n")
            else:
                max_value = max(numbers)  # Находим максимальное значение
                min_value = min(numbers)  # Находим минимальное значение
                f.write(f"Максимальное значение: {max_value}\n")
                f.write(f"Минимальное значение: {min_value}\n")


    except FileNotFoundError:
        print("Файл не найден")
    except Exception as e:
        # Обработка любых исключений
        print(f"Произошла ошибка: {e}")





def line40(f, t):
    try:
        # Открываем файл для чтения
        with open(f, 'r', encoding='utf-8') as infile:
            # Открываем файл для записи
            with open(t, 'w', encoding='utf-8') as outfile:
                content = ''  # Строкф для хранения литер

                for line in infile:
                    if '.' in line:
                        content += line.split('.')[0] # Обрезаем строку до первой точки
                        break  # Выходим из цикла, так как нашли точку
                    else:
                        # Если точки нет, добавляем всю строку к содержимому
                        content += line

                # Удаляем точку из содержимого, если она есть в конце
                content = content.replace('.', '')

                # Записываем содержимое в файл по 40 литер в строке
                for i in range(0, len(content), 40):
                    # Записываем подстроку длиной до 40 литер и добавляем перевод строки
                    outfile.write(content[i:i + 40] + '\n')

    except FileNotFoundError:
        # Обрабатываем случай, если файл не найден
        print(f"Ошибка: Файл '{f}' не найден.")
    except IOError as e:
        # Обрабатываем ошибки ввода-вывода
        print(f"Ошибка ввода-вывода: {e}")
    except Exception as e:
        # Обрабатываем любые другие исключения
        print(f"Произошла ошибка: {e}")







