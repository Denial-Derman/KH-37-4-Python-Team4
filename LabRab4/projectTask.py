# Лабораторна робота 4

# Основний текст
text="Мрії — це крила, що ведуть до нових вершин. Вони завжди дарують натхнення і силу досягати більше!"
print("Текст:\n", text) # Вивід тексту
length=len(text) # Довжина тексту
print("Довжин текста: ", length)

# Вбудовані функції
# Завдов'єв Денис
def cetnerText():
    width = 100  # Ширина поля відносно якого відцентровується текст
    centring= text.center(width) # Повертає вирівнювання рядка по центру
    return centring

def lowerCase():
    lowerCase=text.lower() # Конвертування рядка у нижній регістр
    return lowerCase

def upperCase():
    upperCase=text.upper() # Конвертування рядка у верхній регістр
    return upperCase
# Наступний студент має використати swapcase(), rindex(), find()

# Галиченко Анна

def swapCase():
    swapped_text = text.swapcase()  # Зміна регістру символів на протилежний
    return swapped_text

def rindexChar(char):
    try:
        return text.rindex(char)  # Пошук останньої позиції символу в рядку
    except ValueError:
        return f"Символ '{char}' не знайдено в тексті."

def findSubstring(substring):
    position = text.find(substring)  # Пошук першої позиції підрядка в рядку
    if position != -1:
        return f"Підрядок '{substring}' знайдено на позиції {position}."
    else:
        return f"Підрядок '{substring}' не знайдено в тексті."

# main
print("Центрування:\n", cetnerText())
print("Нижній регістр:\n", lowerCase())
print("Верхній регістр:\n", upperCase())

# main Галиченко
print("Текст з зміненим регістром:\n", swapCase())
print(rindexChar('н'))  # Приклад пошуку останньої позиції символа 'н'
print(findSubstring('крила'))  # Приклад пошуку підрядка 'крила'


