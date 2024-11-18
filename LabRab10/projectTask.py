#  Функція для відкриття файлу у заданому режимі.
def Open(file_name, mode, encoding="utf-8"):
    try:
        file = open(file_name, mode)
    except:
        print(f"Файл {file_name} не було відкрито!")
        return None
    else:
        print(f"Файл {file_name} було відкрито!")
        return file

file_name = "test_python.txt"
file_w = Open(file_name, "w", encoding="utf-8")
# Завдов'єв Денис надання першого питання
if file_w:
    try:
        file_w.write("Прізвище: Завдов'єв\n")
        file_w.write("Питання 1: Що робить цикл for у Python?\n")
        print(f"Файл {file_name} успішно створено!")
    except Exception as e:
        print(f"Помилка при записі у файл {file_name}: {e}")
    finally:
        file_w.close()
        print(f"Файл {file_name} закрито!")

# Читання і друк. Додано з метою виводу тексту з файла
file_r = Open(file_name, "r", encoding="utf-8")
if file_r != None:
    print("\nТестування:")
    for line in file_r:
        print(line.strip())
    file_r.close()
    print(f"\nФайл {file_name} закрито!")