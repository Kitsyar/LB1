import re
import hashlib

def analyze_text(text):
    """
    Приймає рядок тексту, повертає словник з унікальними словами та їх кількістю,
    а також список слів, що зустрічаються більше 3 разів.

    Args:
        text (str): Рядок тексту для аналізу.

    Returns:
        tuple: Кортеж, що містить:
            - dict: Словник, де ключі - унікальні слова, значення - кількість їх появ.
            - list: Список слів, що зустрічаються більше 3 разів.
    """
    # Видаляємо розділові знаки та приводимо до нижнього регістру для ігнорування регістру
    text = re.sub(r'[^\w\s]', '', text).lower()
    words = text.split()

    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    frequent_words = [word for word, count in word_counts.items() if count > 3]

    return word_counts, frequent_words

# Приклад використання:
text_example = "Це приклад тексту, в якому слово приклад зустрічається декілька разів. " \
               "Слово текст також зустрічається тут. І ще раз слово приклад."

word_frequency, frequent_word_list = analyze_text(text_example)

print("Частота зустрічання слів:")
for word, count in word_frequency.items():
    print(f"'{word}': {count}")

print("\nСлова, що зустрічаються більше 3 разів:")
if frequent_word_list:
    print(frequent_word_list)
else:
    print("Такі слова відсутні.")

class Inventory:
    def __init__(self, initial_inventory=None):
        """
        Ініціалізує об'єкт інвентарю.

        Args:
            initial_inventory (dict, optional): Початковий словник інвентарю,
                де ключі - назви продуктів, а значення - їх кількість.
                За замовчуванням None (створюється порожній інвентар).
        """
        if initial_inventory is None:
            self.inventory = {}
        else:
            self.inventory = initial_inventory.copy()

    def update_inventory(self, product_name, quantity_change):
        """
        Оновлює кількість вказаного продукту в інвентарі.

        Args:
            product_name (str): Назва продукту для оновлення.
            quantity_change (int): Зміна кількості.
                Додатне значення - додавання продуктів.
                Від'ємне значення - видалення продуктів.
        """
        if product_name in self.inventory:
            self.inventory[product_name] += quantity_change
            if self.inventory[product_name] < 0:
                print(f"Увага: Кількість продукту '{product_name}' стала від'ємною ({self.inventory[product_name]}).")
            elif self.inventory[product_name] == 0:
                del self.inventory[product_name]  # Видаляємо продукт, якщо кількість стала нуль
        else:
            if quantity_change > 0:
                self.inventory[product_name] = quantity_change
            else:
                print(f"Помилка: Продукт '{product_name}' відсутній на складі, неможливо видалити.")

    def get_low_stock_products(self, threshold=5):
        """
        Повертає список продуктів, кількість яких на складі менше заданого порогу.

        Args:
            threshold (int, optional): Мінімальна кількість для вважання продукту
                таким, що має низький запас. За замовчуванням 5.

        Returns:
            list: Список назв продуктів з низьким запасом.
        """
        low_stock = [product for product, quantity in self.inventory.items() if quantity < threshold]
        return low_stock

    def display_inventory(self):
        """
        Виводить на екран поточний стан інвентарю.
        """
        print("\nПоточний стан інвентарю:")
        if self.inventory:
            for product, quantity in self.inventory.items():
                print(f"- {product}: {quantity} од.")
        else:
            print("Інвентар порожній.")

# Приклад використання:
initial_stock = {"яблука": 10, "банани": 20, "молоко": 5, "хліб": 15}
warehouse = Inventory(initial_stock)

warehouse.display_inventory()

# Додавання продуктів
warehouse.update_inventory("яблука", 5)
warehouse.update_inventory("апельсини", 12)
warehouse.display_inventory()

# Видалення продуктів
warehouse.update_inventory("банани", -8)
warehouse.update_inventory("молоко", -7)
warehouse.display_inventory()

# Отримання списку продуктів з низьким запасом
low_stock_list = warehouse.get_low_stock_products()
print("\nПродукти з низьким запасом (менше 5):", low_stock_list)

# Спроба видалити відсутній продукт
warehouse.update_inventory("печиво", -3)

warehouse.display_inventory()

def calculate_sales_statistics(sales_data):
    """
    Приймає список словників, що представляють продажі, та обчислює статистику доходів.

    Args:
        sales_data (list): Список словників, де кожен словник має ключі:
                           "продукт" (str), "кількість" (int), "ціна" (float).

    Returns:
        tuple: Кортеж, що містить:
            - dict: Словник, де ключі - назви продуктів, а значення - загальний дохід від їх продажу.
            - list: Список назв продуктів, що принесли дохід більший ніж 1000.
    """
    product_total_revenue = {}
    high_revenue_products = []

    for sale in sales_data:
        product = sale["продукт"]
        quantity = sale["кількість"]
        price = sale["ціна"]
        revenue = quantity * price

        product_total_revenue[product] = product_total_revenue.get(product, 0) + revenue

    for product, total_revenue in product_total_revenue.items():
        if total_revenue > 1000:
            high_revenue_products.append(product)

    return product_total_revenue, high_revenue_products

# Приклад використання:
sales = [
    {"продукт": "яблука", "кількість": 50, "ціна": 25.50},
    {"продукт": "банани", "кількість": 100, "ціна": 12.00},
    {"продукт": "яблука", "кількість": 30, "ціна": 25.50},
    {"продукт": "молоко", "кількість": 20, "ціна": 40.00},
    {"продукт": "хліб", "кількість": 150, "ціна": 8.75},
    {"продукт": "банани", "кількість": 80, "ціна": 12.00},
    {"продукт": "кава", "кількість": 10, "ціна": 120.00},
    {"продукт": "чай", "кількість": 25, "ціна": 55.00},
    {"продукт": "яблука", "кількість": 60, "ціна": 26.00},
]

total_revenue_by_product, high_revenue_product_list = calculate_sales_statistics(sales)

print("Загальний дохід для кожного продукту:")
for product, revenue in total_revenue_by_product.items():
    print(f"- {product}: {revenue:.2f} грн.")

print("\nПродукти, що принесли дохід більший ніж 1000 грн.:")
if high_revenue_product_list:
    print(high_revenue_product_list)
else:
    print("Немає продуктів з доходом більшим ніж 1000 грн.")

class TaskManager:
    def __init__(self, initial_tasks=None):
        """
        Ініціалізує об'єкт системи управління задачами.

        Args:
            initial_tasks (dict, optional): Початковий словник задач,
                де ключі - назви задач, а значення - їх статус
                ("виконано", "в процесі", "очікує"). За замовчуванням None.
        """
        if initial_tasks is None:
            self.tasks = {}
        else:
            self.tasks = initial_tasks.copy()

    def add_task(self, task_name, status="очікує"):
        """
        Додає нову задачу до системи.

        Args:
            task_name (str): Назва нової задачі.
            status (str, optional): Початковий статус задачі
                ("виконано", "в процесі", "очікує"). За замовчуванням "очікує".
        """
        if task_name in self.tasks:
            print(f"Увага: Задача '{task_name}' вже існує.")
        else:
            if status in ["виконано", "в процесі", "очікує"]:
                self.tasks[task_name] = status
                print(f"Задача '{task_name}' додана зі статусом '{status}'.")
            else:
                print(f"Помилка: Неправильний статус '{status}'. Допустимі статуси: 'виконано', 'в процесі', 'очікує'.")

    def remove_task(self, task_name):
        """
        Видаляє задачу із системи.

        Args:
            task_name (str): Назва задачі для видалення.
        """
        if task_name in self.tasks:
            del self.tasks[task_name]
            print(f"Задача '{task_name}' видалена.")
        else:
            print(f"Помилка: Задача '{task_name}' не знайдена.")

    def change_task_status(self, task_name, new_status):
        """
        Змінює статус існуючої задачі.

        Args:
            task_name (str): Назва задачі, статус якої потрібно змінити.
            new_status (str): Новий статус задачі ("виконано", "в процесі", "очікує").
        """
        if task_name in self.tasks:
            if new_status in ["виконано", "в процесі", "очікує"]:
                self.tasks[task_name] = new_status
                print(f"Статус задачі '{task_name}' змінено на '{new_status}'.")
            else:
                print(f"Помилка: Неправильний статус '{new_status}'. Допустимі статуси: 'виконано', 'в процесі', 'очікує'.")
        else:
            print(f"Помилка: Задача '{task_name}' не знайдена.")

    def get_pending_tasks(self):
        """
        Повертає список задач, які мають статус "очікує".

        Returns:
            list: Список назв задач зі статусом "очікує".
        """
        pending_tasks = [task for task, status in self.tasks.items() if status == "очікує"]
        return pending_tasks

    def display_tasks(self):
        """
        Виводить на екран поточний список задач та їх статуси.
        """
        print("\nПоточний список задач:")
        if self.tasks:
            for task, status in self.tasks.items():
                print(f"- {task}: {status}")
        else:
            print("Список задач порожній.")

# Приклад використання:
task_manager = TaskManager({"Прибрати кімнату": "виконано", "Написати звіт": "в процесі"})

task_manager.display_tasks()

# Додавання задач
task_manager.add_task("Купити продукти")
task_manager.add_task("Зателефонувати клієнту", "в процесі")
task_manager.add_task("Підготувати презентацію", "очікує")
task_manager.display_tasks()

# Видалення задачі
task_manager.remove_task("Купити продукти")
task_manager.display_tasks()

# Зміна статусу задачі
task_manager.change_task_status("Написати звіт", "виконано")
task_manager.change_task_status("Підготувати презентацію", "в процесі")
task_manager.display_tasks()

# Отримання списку задач, що очікують
pending_tasks_list = task_manager.get_pending_tasks()
print("\nЗадачі, що очікують:", pending_tasks_list)

# Спроба додати задачу з неправильним статусом
task_manager.add_task("Прочитати книгу", "новий")

# Спроба змінити статус неіснуючої задачі
task_manager.change_task_status("Полити квіти", "виконано")

class UserAuthenticator:
    def __init__(self, initial_users=None):
        """
        Ініціалізує об'єкт для аутентифікації користувачів.

        Args:
            initial_users (dict, optional): Початковий словник користувачів,
                де ключі - логіни, а значення - словники з ключами
                "hashed_password" (захешований пароль) та "full_name" (повне ПІБ).
                За замовчуванням None.
        """
        if initial_users is None:
            self.users = {}
        else:
            self.users = initial_users.copy()

    def register_user(self, login, password, full_name):
        """
        Реєструє нового користувача.

        Args:
            login (str): Логін користувача.
            password (str): Пароль користувача (буде захешований).
            full_name (str): Повне ПІБ користувача.
        """
        if login in self.users:
            print(f"Помилка: Користувач з логіном '{login}' вже існує.")
        else:
            hashed_password = self._hash_password(password)
            self.users[login] = {"hashed_password": hashed_password, "full_name": full_name}
            print(f"Користувач '{login}' успішно зареєстрований.")

    def _hash_password(self, password):
        """
        Хешує пароль за допомогою алгоритму MD5.

        Args:
            password (str): Пароль для хешування.

        Returns:
            str: Захешований пароль у шістнадцятковому форматі.
        """
        hashed_password = hashlib.md5(password.encode('utf-8')).hexdigest()
        return hashed_password

    def verify_password(self, login):
        """
        Перевіряє введений користувачем пароль.

        Args:
            login (str): Логін користувача.

        Returns:
            bool: True, якщо пароль введено правильно, False - якщо ні або користувача не знайдено.
        """
        if login in self.users:
            entered_password = input(f"Введіть пароль для користувача '{login}': ")
            hashed_entered_password = self._hash_password(entered_password)
            if hashed_entered_password == self.users[login]["hashed_password"]:
                print(f"Аутентифікація успішна для користувача '{login}'.")
                print(f"Повне ім'я: {self.users[login]['full_name']}")
                return True
            else:
                print("Помилка: Неправильний пароль.")
                return False
        else:
            print(f"Помилка: Користувача з логіном '{login}' не знайдено.")
            return False

# Приклад використання:
authenticator = UserAuthenticator()

# Реєстрація користувачів
authenticator.register_user("jane_doe", "password123", "Джейн Доу")
authenticator.register_user("johny_depp", "securePass", "Джонні Депп")

# Спроба реєстрації існуючого користувача
authenticator.register_user("jane_doe", "anotherPass", "Джейн Доу молодша")

print("\nАутентифікація користувачів:")
# Перевірка пароля
authenticator.verify_password("jane_doe")
authenticator.verify_password("johny_depp")

# Спроба аутентифікації з неправильним паролем
authenticator.verify_password("jane_doe")

# Спроба аутентифікації неіснуючого користувача
authenticator.verify_password("lemmy_kilmister")
