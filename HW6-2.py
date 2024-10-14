def get_cats_info(path):
    try:
        # Використовуємо менеджер контексту для відкриття файлу
        with open(path, 'r', encoding='utf-8') as file:
            cats = []  # Список для зберігання інформації про котів
            
            # Читаємо кожен рядок файлу
            for line in file:
                # Видаляємо зайві пробіли та символи нового рядка
                line = line.strip()
                
                # Розділяємо рядок за комою, щоб отримати ідентифікатор, ім'я та вік
                parts = line.split(',')
                if len(parts) == 3:
                    # Створюємо словник з ключами "id", "name" та "age"
                    cat_info = {
                        "id": parts[0],
                        "name": parts[1],
                        "age": parts[2]
                    }
                    # Додаємо словник до списку котів
                    cats.append(cat_info)
        
            # Повертаємо список словників
            return cats
    
    # Обробляємо виняток, якщо файл не знайдено
    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
        return []

# Приклад використання функції
cats_info = get_cats_info("path/to/cats_file.txt")
print(cats_info)
