from collections import deque

# Функція для перевірки, чи є рядок паліндромом
def is_palindrome(input_string):
    # Видаляємо пробіли та приводимо рядок до нижнього регістру
    cleaned_string = ''.join(input_string.split()).lower()

    # Створюємо двосторонню чергу (deque) для символів
    char_queue = deque(cleaned_string)

    # Перевіряємо, чи є рядок паліндромом
    while len(char_queue) > 1:
        # Порівнюємо символи з обох кінців черги
        if char_queue.popleft() != char_queue.pop():
            return False

    return True

# Приклад використання
input_str1 = "A man a plan a canal Panama"
input_str2 = "Hello, World!"

print(f"'{input_str1}' є паліндромом? : {is_palindrome(input_str1)}")  # Виведе: True
print(f"'{input_str2}' є паліндромом? : {is_palindrome(input_str2)}")  # Виведе: False
