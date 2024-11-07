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

#main
print("\t\t<*> Програма запущена <*>\n")
print("\t\t* Правило написання ключа *"
      "\n\tКлюч  пишеться за правилом: \n\tПерше число:  номер групи, якщо номер однозначний, то пишеться з 0 (Наприклад:05)\n"
      "\tДруге число: порядковий номер згадування групи в словнику*")
while True:
    choice = input("\n\t\t* Навігаційне меню *\n> Введіть 1, для виведення даних словника\n"
                   "> Пункт не зазначено\n" # Дописувати відповідний номер пункту для виконання функції
                   # Наступний пункт: Додавання нового запису до словника з первіркою на вірно введений ключ та курсу
                   "> Введіть 0, щоб закінчити\n"
                   "> Введення пункту: ")

    if choice == '1':
        print("\n\t\t* Вивід складу словника *")
        display_students()

    elif choice == '0':
        print("\t\t<*> Програма завершена <*>")
        break
    else:
        print("> Незареєстрована дія. Спробуйте ще раз. <")
