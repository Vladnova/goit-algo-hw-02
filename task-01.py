import queue
import time
import random

# Створення черги для заявок
request_queue = queue.Queue()

# Функція для генерації нових заявок
def generate_request():
    # Створюємо заявку з унікальним номером
    request_id = random.randint(1000, 9999)
    request = f"Заявка {request_id}"
    print(f"Згенеровано нову заявку: {request}")

    # Додаємо заявку до черги
    request_queue.put(request)

# Функція для обробки заявок
def process_request():
    if not request_queue.empty():
        # Видаляємо заявку з черги
        request = request_queue.get()
        print(f"Обробка заявки: {request}")
    else:
        print("Черга пуста. Немає заявок для обробки.")

# Головний цикл програми
def main():
    while True:
        # Генерація нових заявок
        generate_request()

        # Обробка заявок
        process_request()

        # Затримка для імітації часу між заявками
        time.sleep(0.3)

# Запуск програми
if __name__ == "__main__":
    main()
