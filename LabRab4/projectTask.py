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

# Kucheriavenko-R-B
def joinWords(word_list):
    # Об'єднання слів у один рядок з пробілами
    joined_text = ' '.join(word_list)
    return joined_text

def justifyRight(text, width):
    # Додавання пробілів для вирівнювання тексту праворуч
    right_justified = text.rjust(width)
    return right_justified

def translateText(text, translation_table):
    # Переклад символів у тексті згідно з переданою таблицею замін
    translated_text = text.translate(translation_table)
    return translated_text

# Савченко
def rightSplit(separator=" "):
    # Розділяє рядок на список, починаючи з правого кінця, за вказаним роздільником
    rsplit_text = text.rsplit(separator)
    return rsplit_text

def rightStrip():
    # Видаляє пробіли або символи з правого краю рядка
    rstrip_text = text.rstrip()
    return rstrip_text

def splitText(separator=" "):
    # Розділяє рядок на список за вказаним роздільником
    split_text = text.split(separator)
    return split_text

#Білокур
def is_palindrome(text):
  # Видаляємо всі пробіли та розділові знаки і приводимо до нижнього регістру
  cleaned_text = ''.join(c for c in text if c.isalnum()).lower()
  return cleaned_text == cleaned_text[::-1]
from collections import Counter

def word_frequency(text):
  words = text.split()
  return Counter(words)

def replace_vowels(text, replacement):
  vowels = "aeiouyAEIOUY"
  translation_table = str.maketrans(vowels, replacement * len(vowels))
  return text.translate(translation_table)

# main
print("Центрування:\n", cetnerText())
print("Нижній регістр:\n", lowerCase())
print("Верхній регістр:\n", upperCase())

# main Галиченко
print("Текст з зміненим регістром:\n", swapCase())
print(rindexChar('н'))  # Приклад пошуку останньої позиції символа 'н'
print(findSubstring('крила'))  # Приклад пошуку підрядка 'крила'

# main Kycheriavenko
# Використання функції joinWords
words = text.split()
joined_text = joinWords(words)
print(joined_text)  # Мрії — це крила, що ведуть до нових вершин. Вони завжди дарують натхнення і силу досягати більше!

# Використання функції justifyRight
justified_text = justifyRight(joined_text, 100)
print(justified_text)  # Добавлення пробілів для вирівнювання праворуч

# Використання функції translateText
translation_table = str.maketrans("аеиор", "43105")
translated_text = translateText(joined_text, translation_table)
print(translated_text)

#main Савченко
print(rightSplit())
print(rightStrip())
print(splitText())

#main Білокур
print(is_palindrome(text))
word_counts = word_frequency(text)
print(word_counts)
new_text = replace_vowels(text, 'x')
print(new_text)