import sys
from pathlib import Path
from colorama import init, Fore, Style

# Ініціалізуємо бібліотеку colorama для підтримки кольорів у виведенні
init(autoreset=True)

def display_directory_structure(path, indent_level=0):
    try:
        # Створюємо об'єкт Path для роботи з шляхом до директорії
        directory = Path(path)

        # Перевіряємо, чи існує вказаний шлях і чи є він директорією
        if not directory.exists() or not directory.is_dir():
            print(Fore.RED + f"Шлях '{path}' не існує або не є директорією.")
            return

        # Обходимо всі елементи в директорії
        for item in directory.iterdir():
            # Формуємо відступ для візуального відображення вкладеності
            indent = '    ' * indent_level

            if item.is_dir():
                # Якщо це директорія, виводимо її назву в синьому кольорі
                print(indent + Fore.BLUE + f"📂 {item.name}")
                # Викликаємо функцію рекурсивно для вкладених директорій
                display_directory_structure(item, indent_level + 1)
            else:
                # Якщо це файл, виводимо його назву в зеленому кольорі
                print(indent + Fore.GREEN + f"📜 {item.name}")

    except Exception as e:
        # Обробка інших помилок
        print(Fore.RED + f"Помилка при обробці директорії: {e}")

if __name__ == "__main__":
    # Перевіряємо, чи вказано шлях до директорії як аргумент командного рядка
    if len(sys.argv) < 2:
        print(Fore.RED + "Будь ласка, вкажіть шлях до директорії.")
    else:
        # Отримуємо шлях з аргументів командного рядка
        directory_path = sys.argv[1]
        # Викликаємо функцію для відображення структури директорії
        display_directory_structure(directory_path)
