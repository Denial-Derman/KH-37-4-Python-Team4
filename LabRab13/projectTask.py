import csv
import json

# Оновлені дані
students_data = {
    "0170": {
        "Прізвище": "Завдов'єв",
        "Ім'я": "Денис",
        "Адреса": "пр. Михайла Лушпи, 18",
        "Номер школи": 17,
        "Клас": 9
    },
    "0070": {
        "Прізвище": "Петренко",
        "Ім'я": "Петро",
        "Адреса": "вул. Лесі Українки, 25",
        "Номер школи": 7,
        "Клас": 9
    },
    "0171": {
        "Прізвище": "Сидоренко",
        "Ім'я": "Оксана",
        "Адреса": "пр. Михайла Лушпи, 18",
        "Номер школи": 17,
        "Клас": 11
    }
}

# Перетворюємо дані для запису у CSV
students_list = []
for student_id, student_info in students_data.items():
    student_info["id"] = student_id  # Додаємо id як окремий елемент
    students_list.append(student_info)

# Функція для запису даних у CSV файл
def write_csv(csv_filename, data):
    try:
        with open(csv_filename, mode='wt', newline='', encoding='utf-8') as csv_file:
            fieldnames = data[0].keys()  # Використовуємо ключі з першого словника
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_writer.writeheader()
            csv_writer.writerows(data)
        # Повідомлення про успішний запис
        print(f"Дані успішно записані у файл '{csv_filename}'.")
    except Exception as e:
        print(f"Сталася помилка при запису у CSV: {e}")

# Функція для запису даних у JSON файл
def write_json(json_filename, data):
    try:
        with open(json_filename, mode='wt', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)
        # Повідомлення про успішний запис
        print(f"Дані успішно записані у файл '{json_filename}'.")
    except Exception as e:
        print(f"Сталася помилка при запису у JSON: {e}")

# Функція для читання з CSV файлу та виведення даних
def read_csv(csv_filename):
    try:
        with open(csv_filename, mode='rt', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            print(f"\nДані з файлу {csv_filename}:")
            for row in csv_reader:
                print(row)
    except Exception as e:
        print(f"Сталася помилка при читанні CSV: {e}")

# Функція для читання з JSON файлу та виведення даних
def read_json(json_filename):
    try:
        with open(json_filename, mode='rt', encoding='utf-8') as json_file:
            data = json.load(json_file)
            print(f"\nДані з файлу {json_filename}:")
            print(json.dumps(data, indent=4, ensure_ascii=False))
    except Exception as e:
        print(f"Сталася помилка при читанні JSON: {e}")

# Спочатку записуємо дані у .csv файл
write_csv('student.csv', students_list)

# Потім перезаписуємо ті ж самі дані у .json файл
write_json('student.json', students_data)

# Тепер читаємо та виводимо дані з обох файлів
read_csv('student.csv')
read_json('student.json')
