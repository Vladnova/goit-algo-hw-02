def check_brackets(expression):
    # Стек для зберігання відкритих дужок
    stack = []

    # Словник для перевірки парності символів
    matching_brackets = {')': '(', '}': '{', ']': '['}

    # Проходимо через кожен символ виразу
    for char in expression:
        if char in '({[':
            # Додаємо відкриті дужки в стек
            stack.append(char)
        elif char in ')}]':
            # Якщо зустрічаємо закриту дужку, перевіряємо її пару
            if stack and stack[-1] == matching_brackets[char]:
                # Якщо пари правильні, видаляємо верхній елемент зі стеку
                stack.pop()
            else:
                # Якщо пари неправильні, або стек порожній
                return "Несиметрично"

    # Якщо стек порожній, всі дужки правильно закриті
    if not stack:
        return "Симетрично"
    else:
        # Якщо залишилися відкриті дужки в стеці
        return "Несиметрично"

# Приклад використання
expression1 = "( ){[ 1 ]( 1 + 3 )( ){ }}"
expression2 = "( 23 ( 2 - 3);"
expression3 = "( 11 }"

print(f"'{expression1}' : {check_brackets(expression1)}")  # Виведе: Симетрично
print(f"'{expression2}' : {check_brackets(expression2)}")  # Виведе: Несиметрично
print(f"'{expression3}' : {check_brackets(expression3)}")  # Виведе: Несиметрично
