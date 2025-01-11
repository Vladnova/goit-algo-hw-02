# Програма для обробки заявок, перевірки паліндромів та симетрії розділювачів

Ця програма включає три завдання для роботи з чергами та стеком в Python.

## Завдання 1: Імітація обробки заявок

Програма імітує приймання та обробку заявок за допомогою черги (`Queue` з модуля `queue`). Вона автоматично генерує нові заявки, додає їх до черги, а потім послідовно видаляє з черги для обробки. Це імітує роботу сервісного центру.

### Алгоритм:
1. Створюється черга заявок.
2. Функція `generate_request()` генерує нову заявку та додає її до черги.
3. Функція `process_request()` обробляє заявку, видаляючи її з черги.
4. Головний цикл програми генерує нові заявки та обробляє їх до завершення роботи програми.

### Реалізація:

```
import queue

# Створення черги заявок
queue = queue.Queue()

# Функція генерації заявки
def generate_request():
    # Створення нової заявки
    # Додавання заявки до черги
    pass

# Функція обробки заявки
def process_request():
    # Перевірка чи черга пуста
    if not queue.empty():
        # Обробка заявки
        queue.get()
    else:
        print("Черга пуста")

# Головний цикл програми
while True:
    generate_request()
    process_request()
```

## Завдання 2: Перевірка паліндрома

Це завдання передбачає розробку функції, яка приймає рядок як вхідний параметр і перевіряє, чи є цей рядок паліндромом. Для цього використовується двостороння черга (`deque` з модуля `collections` в Python). Програма порівнює символи з обох кінців черги, ігнорує регістр та пробіли.

### Алгоритм:
1. Спочатку необхідно видалити всі пробіли з рядка та привести його до нижнього регістру для коректної перевірки (нечутливість до регістру).
2. Кожен символ рядка додається до двосторонньої черги.
3. Потім програма порівнює символи з обох кінців черги:
   - Якщо символи зліва і справа однакові, програма продовжує порівняння.
   - Якщо символи різні, рядок не є паліндромом.
4. Якщо всі пари символів однакові, рядок є паліндромом.

### Реалізація:

```
from collections import deque

def is_palindrome(input_string):
    # Видалення пробілів і переведення в нижній регістр
    cleaned_string = input_string.replace(" ", "").lower()
    
    # Створення двосторонньої черги
    dq = deque(cleaned_string)
    
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True
```
### Приклад використання:
```
result = is_palindrome("A man a plan a canal Panama")
print(result)  # Виведе: True

result = is_palindrome("Hello World")
print(result)  # Виведе: False
```

## Завдання 3: Перевірка симетрії розділювачів

Це завдання передбачає написання програми, яка перевіряє правильність і симетрію розділювачів у рядку. В програма використовується стек для зберігання відкритих розділювачів і перевірки, чи є вони симетричними, чи не мають помилок, таких як несумісні пари розділювачів або неправильно закриті дужки.

### Алгоритм:
1. Програма аналізує рядок, що складається з різних видів дужок: круглих `()`, квадратних `[]` і фігурних `{}`.
2. Вона використовує стек для збереження відкритих розділювачів.
3. Кожен символ рядка перевіряється:
    - Якщо це відкриваюча дужка, вона додається до стека.
    - Якщо це закриваюча дужка, перевіряється, чи є відповідна відкрита дужка на вершині стека. Якщо це так, дужка знімається з стека.
    - Якщо немає відповідної відкритої дужки або дужка неправильно закрита, рядок вважається несиметричним.
4. Після обробки всього рядка стек повинен бути порожнім, щоб всі відкриті дужки були правильно закриті.

### Реалізація:

```
def check_brackets_balance(input_string):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for char in input_string:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack[-1] != pairs[char]:
                return "Несиметрично"
            stack.pop()
    
    return "Симетрично" if not stack else "Несиметрично"
```

### Приклад використання:

```
result = check_brackets_balance("( ){[ 1 ]( 1 + 3 )( ){ }}")
print(result)  # Виведе: Симетрично

result = check_brackets_balance("( 23 ( 2 - 3);")
print(result)  # Виведе: Несиметрично

result = check_brackets_balance("( 11 }")
print(result)  # Виведе: Несиметрично

```