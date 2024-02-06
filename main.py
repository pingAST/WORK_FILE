def create_cook_book(file_name):
    cook_book = {}
    
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        
        i = 0
        while i < len(lines):
            dish_name = lines[i].strip()
            ingredient_count = 0
            if lines[i+1].strip().isdigit():
                ingredient_count = int(lines[i+1])
            else:
                i += 1
                continue

            ingredients = []
            
            for j in range(i+2, i+2+ingredient_count):
                ingredient_info = lines[j].strip().split(' | ')
                ingredient = {
                    'ingredient_name': ingredient_info[0],
                    'quantity': int(ingredient_info[1]),
                    'measure': ingredient_info[2]
                }
                ingredients.append(ingredient)
            
            cook_book[dish_name] = ingredients
            i += 2 + ingredient_count
    
    return cook_book

file_name = 'recipes.txt'
cook_book = create_cook_book(file_name)

cook_book_output = {}
for dish, ingredients in cook_book.items():
    cook_book_output[dish] = []
    for ingredient in ingredients:
        ingredient_output = {
            'ingredient_name': ingredient['ingredient_name'],
            'quantity': ingredient['quantity'],
            'measure': ingredient['measure']
        }
        
        cook_book_output[dish].append(ingredient_output)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                name = ingredient['ingredient_name']
                measure = ingredient['measure']
                quantity = ingredient['quantity'] * person_count
                
                if name not in shop_list:
                    shop_list[name] = {'measure': measure, 'quantity': quantity}
                else:
                    shop_list[name]['quantity'] += quantity
    sorted_shop_list = dict(sorted(shop_list.items()))
    
    return sorted_shop_list

def merge_files(file_names):
    file_contents = []
    for file_name in file_names:
        with open(file_name, 'r', encoding= "utf-8") as file:
            content = file.read()
            lines = content.split('\n')
            file_contents.append((file_name, content, len(lines)))

    file_contents.sort(key=lambda x: x[2])

    with open('result.txt', 'w', encoding= "utf-8") as result_file:
        for file_name, content, _ in file_contents:
            result_file.write(f"{file_name}\n{len(content.splitlines())}\n{content}\n")

    print()
    print("Файл успешно создан: result.txt")

#Задача №1
print("cook_book = {")
for dish, ingredients in cook_book_output.items():
    print(f"  '{dish}': [")
    for ingredient in ingredients:
        print(f"    {{'ingredient_name': '{ingredient['ingredient_name']}', 'quantity': {ingredient['quantity']}, 'measure': '{ingredient['measure']}'}}")
    print("    ],")
print("}")

print()

#Задача №2
result = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
print("{")
for ingredient, details in result.items():
    print(f"  '{ingredient}': {{'measure': '{details['measure']}', 'quantity': {details['quantity']}}},")
print("}")

#Задача №3
merge_files(['1.txt', '2.txt', '3.txt'])
