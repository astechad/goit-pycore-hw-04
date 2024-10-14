def total_salary(path):
    try:
        # Використовуємо менеджер контексту для відкриття файлу
        with open(path, 'r', encoding='utf-8') as file:
            salaries = []
            
            # Читаємо кожен рядок у файлі
            for line in file:
                # Видаляємо зайві пробіли та символи нового рядка
                line = line.strip()
                
                # Розділяємо прізвище та зарплату за комою
                parts = line.split(',')
                if len(parts) == 2:
                    # Пробуємо конвертувати зарплату в число
                    try:
                        salary = float(parts[1])
                        salaries.append(salary)
                    except ValueError:
                        print(f"Неможливо перетворити зарплату на число: {parts[1]}")
            
            # Обчислюємо загальну та середню зарплати
            total = sum(salaries)
            average = total / len(salaries) if salaries else 0
            
            # Повертаємо результат як кортеж
            return total, average
    
    # Обробляємо виняток, якщо файл не знайдено
    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
        return None, None

# Приклад використання функції
total, average = total_salary("path/to/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
