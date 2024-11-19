#  Функція для відкриття файлу у заданому режимі.
def Open(file_name, mode):
    try:
        file = open(file_name, mode)
    except:
        print(f"Файл {file_name} не було відкрито!")
        return None
    else:
        print(f"Файл {file_name} було відкрито!")
        return file

file_name = "test_python.txt"
file_w = Open(file_name, "w")
# Завдов'єв Денис надання першого питання
if file_w:
    try:
        file_w.write("Студент: Завдов'єв Денис\n")
        file_w.write("Питання 1): Що робить цикл for у Python?\n")
        print(f"Файл {file_name} успішно створено!")
    except Exception as e:
        print(f"Помилка при записі у файл {file_name}: {e}")
    finally:
        file_w.close()
        print(f"Файл {file_name} закрито!")

# Місце для інших студентів
#Савченко Сергій
file_a = Open(file_name, "a")  # Використовуємо режим append
if file_a:
    try:
        file_a.write("\nСтудент: Савченко Сергій\n")
        file_a.write("Відповідь 1): Цикл `for` у Python використовується для проходу по кожному елементу в послідовності і виконання певного коду для кожного з них.\n")
        file_a.write("Питання 2): Що робить функція len() у Python?\n")
    except Exception as e:
        print(f"Помилка при записі у файл {file_name}: {e}")
    finally:
        file_a.close()
        print(f"Файл {file_name} закрито!")

#Галиченко Анна
file_a = Open(file_name, "a")  # Використовуємо режим append
if file_a:
    try:
        file_a.write("\nСтудентка: Галиченко Анна\n")
        file_a.write("Відповідь 2): Функція len() у Python використовується для отримання довжини (кількості елементів) об'єкта, який підтримує цю операцію.\n")
        file_a.write("Питання 3): Як у Python створити словник і додати в нього пару ключ-значення?\n")
    except Exception as e:
        print(f"Помилка при записі у файл {file_name}: {e}")
    finally:
        file_a.close()
        print(f"Файл {file_name} закрито!")

#Кучерявенко Роман
file_a = Open(file_name, "a")  # Використовуємо режим append
if file_a:
    try:
        file_a.write("\nСтудент: Кучерявенко Роман\n")
        file_a.write("Відповідь 3): Створити словник у Python можна за допомогою фігурних дужок {}, а додати пару ключ-значення — через присвоєння значення за ключем або методом update().\n")
        file_a.write("Питання 4): Як у Python вивести текст на екран?\n")
    except Exception as e:
        print(f"Помилка при записі у файл {file_name}: {e}")
    finally:
        file_a.close()
        print(f"Файл {file_name} закрито!")

# Читання і друк. Додано з метою виводу тексту з файла
file_r = Open(file_name, "r")
if file_r != None:
    print("\nТестування:")
    for line in file_r:
        print(line.strip())
    file_r.close()
    print(f"\nФайл {file_name} закрито!")