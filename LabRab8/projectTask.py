# Лабораторна робота №8
items_list=["Алгоритми і структури даних",
            "Англійська мова",
            "Математичні методи дослідження операцій",
            "Психологія",
            "Організація ІТ-бізнесу",
            "Програмування мовою Python",
            "Чисельні методи"]

students = {
    "3700": {"LastName": "Завдов'єв", "FirstName": "Денис", "Patronymic": "Олександрович", "GroupNumber": "КН-37-4", "Course": 2,
         "Subjects": items_list, "Grades": [4,3,5,3,5,5,5]},
    "3701": {"LastName": "Білокур", "FirstName": "Катерина", "Patronymic": "Віталіївна", "GroupNumber": "КН-37-4", "Course": 2,
         "Subjects": items_list, "Grades": [4,5,5,4,4,5,4]},
    "3702": {"LastName": "Галиченко", "FirstName": "Анна", "Patronymic": "Олександрович", "GroupNumber": "КН-37-4", "Course": 2,
         "Subjects": items_list, "Grades": [5,4,5,3,5,5,4]},
    "3703": {"LastName": "Кучерявенко", "FirstName": "Роман", "Patronymic": "Богданович", "GroupNumber": "КН-37-4", "Course": 2,
         "Subjects": items_list, "Grades": [3,5,3,4,4,4,3]},
    "3704": {"LastName": "Савченко", "FirstName": "Сергій", "Patronymic": "Сергійович", "GroupNumber": "КН-37-4", "Course": 2,
         "Subjects": items_list, "Grades": [5,4,5,3,5,5,5]},
}
#def
#функція display_students() виконана студентом Завдов'євом Денисом
def display_students():
    for key, data in students.items():
        print("Ключ:\t Прізвище: Ім'я: По батькові:\t Група:\t Курс:")
        print(f"{key} —\t{data['LastName']} {data['FirstName']} {data['Patronymic']}\t {data['GroupNumber']} {data['Course']}")
        print("Предмети та оцінки:")

        # Виводимо предмети та оцінки в стовпчик
        for subject, grade in zip(data["Subjects"], data["Grades"]):
            print(f"\t{subject}: {grade}")

        print()
#GALICHENKO
def add_student():
    print("\n\t\t* Додавання нового студента *")

    # Отримуємо ключ для нового студента
    student_id = input("Введіть унікальний ключ студента (наприклад, 3705): ")

    # Перевіряємо, чи ключ вже існує
    if student_id in students:
        print("> Помилка: студент з таким ключем вже існує. Спробуйте інший ключ.")
        return

    # Вводимо дані студента
    last_name = input("Введіть прізвище студента: ")
    first_name = input("Введіть ім'я студента: ")
    patronymic = input("Введіть по батькові студента: ")
    group_number = input("Введіть номер групи студента (наприклад, КН-37-4): ")

    # Перевіряємо, чи курс є числом
    try:
        course = int(input("Введіть курс студента (наприклад, 2): "))
        if course < 1 or course > 6:
            print("> Помилка: курс має бути числом від 1 до 6.")
            return
    except ValueError:
        print("> Помилка: курс має бути числом.")
        return

    # Вводимо оцінки студента для кожного предмета
    grades = []
    for subject in items_list:
        try:
            grade = int(input(f"Введіть оцінку з предмету '{subject}' (від 1 до 5): "))
            if grade < 1 or grade > 5:
                print("> Помилка: оцінка має бути в діапазоні від 1 до 5.")
                return
            grades.append(grade)
        except ValueError:
            print("> Помилка: оцінка має бути числом.")
            return

    # Додаємо нового студента в словник
    students[student_id] = {
        "LastName": last_name,
        "FirstName": first_name,
        "Patronymic": patronymic,
        "GroupNumber": group_number,
        "Course": course,
        "Subjects": items_list,
        "Grades": grades
    }
    print("> Студент успішно доданий!")

#Білокур
def sort_students(criteria):
    print("\n\t\t* Сортування студентів за критерієм *")
    sorted_students = []

    if criteria == "ключ":
        sorted_students = sorted(students.items(), key=lambda x: x[0])
    elif criteria == "ім'я":
        sorted_students = sorted(students.items(), key=lambda x: x[1]['FirstName'])
    elif criteria == "прізвище":
        sorted_students = sorted(students.items(), key=lambda x: x[1]['LastName'])
    elif criteria == "курс":
        sorted_students = sorted(students.items(), key=lambda x: x[1]['Course'])
    else:
        print("> Помилка: невідомий критерій сортування.")
        return

    # Виводимо відсортованих студентів
    for key, data in sorted_students:
        print("Ключ:\t Прізвище: Ім'я: По батькові:\t Група:\t Курс:")
        print(f"{key} —\t{data['LastName']} {data['FirstName']} {data['Patronymic']}\t {data['GroupNumber']} {data['Course']}")
        print("Предмети та оцінки:")
        for subject, grade in zip(data["Subjects"], data["Grades"]):
            print(f"\t{subject}: {grade}")
        print()
#Савченко
def remove_student(students, first_name, last_name):
    found = False
    for student_id, student_info in list(students.items()):
        if student_info['FirstName'] == first_name and student_info['LastName'] == last_name:
            del students[student_id]
            print(f"Студента '{first_name} {last_name}' успішно видалено.")
            found = True
            break
    if not found:
        print(f"Студента '{first_name} {last_name}' не знайдено у списку.")
#Kucheriavenko
def find_students_by_grade(students, subject_name, grade):
    # Знаходимо індекс предмета
    if subject_name not in items_list:
        print("Цей предмет не знайдено в списку.")
        return

    subject_index = items_list.index(subject_name)
    found_students = []

    # Шукаємо студентів із заданою оцінкою за цей предмет
    for student_info in students.values():
        if student_info["Grades"][subject_index] == grade:
            full_name = f"{student_info['LastName']} {student_info['FirstName']} {student_info['Patronymic']}"
            found_students.append(full_name)

    # Виводимо результат
    if found_students:
        print(f"Студенти з оцінкою {grade} за предмет '{subject_name}':")
        for student in found_students:
            print(student)
    else:
        print(f"Немає студентів з оцінкою {grade} за предмет '{subject_name}'.")
#main
print("\t\t<*> Програма запущена <*>\n")
print("\t\t* Правило написання ключа *"
      "\n\tКлюч  пишеться за правилом: \n\tПерше число:  номер групи, якщо номер однозначний, то пишеться з 0 (Наприклад:05)\n"
      "\tДруге число: порядковий номер згадування групи в словнику*")
while True:
    choice = input("\n\t\t* Навігаційне меню *\n> Введіть 1, для виведення даних словника\n"
                   "> Введіть 2, для додавання нового студента\n" # Дописувати відповідний номер пункту для виконання функції
                   "> Введіть 3, для сортування студентів за критерієм\n"
                   "> Введіть 4, для видалення студента\n"
                   "> Введіть 5, для пошуку студентів, що мають задану оцінку за дисципліною, введену користувачем\n" 
                   "> Введіть 0, щоб закінчити\n"
                   "> Введення пункту: ")

    if choice == '1':
        print("\n\t\t* Вивід складу словника *")
        display_students()
    elif choice == '2':
        print("\n\t\t* Додавання нового студента *")
        add_student()
    elif choice == '3':
        print("\n\t\t* Сортування за критерієм *")
        criteria = input("> Введіть критерій для сортування (ключ, ім'я, прізвище, курс): ").strip().lower()
        sort_students(criteria)
    elif choice == '4':
        print("\n\t\t* Видалення студента *")
        first_name = input("> Введіть ім'я студента: ").strip()
        last_name = input("> Введіть прізвище студента: ").strip()
        remove_student(students, first_name, last_name)
    elif choice == '5':
        print("\n\t\t* Пошук студента *")
        subject = input("Введіть назву предмета: ")
        grade = int(input("Введіть оцінку для пошуку: "))
        find_students_by_grade(students, subject, grade)
    elif choice == '0':
        print("\t\t<*> Програма завершена <*>")
        break
    else:
        print("> Незареєстрована дія. Спробуйте ще раз. <")
