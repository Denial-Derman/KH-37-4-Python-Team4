import csv
import json

# Дані
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

# Функції Завдов'єва Дениса
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

# Функції наступних студентів
# Галиченко Анна
# переписати дані з JSON у CSV, додавши нові рядки
def json_to_csv1(csv_filename, json_filename, new_data):
    try:
        # Читаємо дані з JSON
        with open(json_filename, mode='rt', encoding='utf-8') as json_file:
            data = json.load(json_file)

        # Перетворюємо дані з JSON в список для запису у CSV
        students_list = []
        for student_id, student_info in data.items():
            student_info["id"] = student_id
            students_list.append(student_info)

        # Додаємо нові дані до списку
        students_list.extend(new_data)

        # Записуємо оновлений список у CSV
        write_csv(csv_filename, students_list)
        print(f"Дані успішно переписані з {json_filename} у {csv_filename}, додано нові рядки.")
    except Exception as e:
        print(f"Сталася помилка при переписуванні з JSON у CSV: {e}")

#Білокур Катерина
#переписати дані з CSV у JSON, додавши нові рядки
def csv_to_json1(json_filename, csv_filename, new_data):
    try:
        # Читаємо дані з CSV
        with open(csv_filename, mode='rt', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = {}
            for row in csv_reader:
                student_id = row["id"]
                data[student_id] = row

        # Додаємо нові дані
        for new_student in new_data:
            data[new_student["id"]] = new_student

        # Записуємо оновлений словник у JSON
        write_json(json_filename, data)
        print(f"Дані успішно переписані з {csv_filename} у {json_filename}, додано нові рядки.")
    except Exception as e:
        print(f"Сталася помилка при переписуванні з CSV у JSON: {e}")

# Завдов'єв Денис запис:
# Спочатку записуємо дані у .csv файл
write_csv('student.csv', students_list)

# Потім перезаписуємо ті ж самі дані у .json файл
write_json('student.json', students_data)

# інші студенти
# Галиченко АНя
new_csv1 = [
     {"Прізвище": "Ковальчук", "Ім'я": "Олег", "Адреса": "вул. Лесі Українки, 25", "Номер школи": 7, "Клас": 10, "id": "0071"},
     {"Прізвище": "Гончаренко", "Ім'я": "Анна", "Адреса": "пр. Михайла Лушпи, 18", "Номер школи": 17, "Клас": 8, "id": "0172"}
 ]
json_to_csv1('student.csv', 'student.json', new_csv1)

#Білокур Катерина
new_json1 = [
    {"Прізвище": "Іваненко", "Ім'я": "Іван", "Адреса": "вул. Герасима Кондратьєва, 136", "Номер школи": 1, "Клас": 10, "id": "0010"},
    {"Прізвище": "Петренко", "Ім'я": "Петро", "Адреса": "пр. Михайла Лушпи, 18", "Номер школи": 17, "Клас": 9, "id": "0173"}
]
csv_to_json1('student.json', 'student.csv', new_json1)


# Тепер читаємо та виводимо дані з обох файлів
read_csv('student.csv')
read_json('student.json')
