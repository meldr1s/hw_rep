def get_cats_info(path):
    cats_info = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    cat_id, name, age = line.strip().split(',')
                    cats_info.append({
                        "id": cat_id,
                        "name": name,
                        "age": age
                    })
                except ValueError:
                    print(f"Невірний формат даних у рядку: {line}")
        
        return cats_info

    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
        return []
        
cats_info = get_cats_info(r"C:\Users\ADMIN\Downloads\python\First_repo\hw4.2\path.txt")
print(cats_info)