def total_salary(path):
    try:
        total = 0
        count = 0
        
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    name, salary = line.strip().split(',')
                    total += int(salary)
                    count += 1
                except ValueError:
                    print(f"Невірний формат даних у рядку: {line}")
        
        if count > 0:
            average_salary = total / count
        else:
            average_salary = 0
        
        return (total, average_salary)

    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
        return (0, 0)


total, average = total_salary(r"C:\Users\ADMIN\Downloads\python\First_repo\hw4.1\path.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")