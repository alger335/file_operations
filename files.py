cook_book = {}
def get_cook_book():
    with open('recipes.txt', encoding='UTF-8') as f:
        for line in f:
            dish_name = line.strip()
            counter = int(f.readline().strip())
            list_of_ingredients = []
            for _ in range(counter):
                ingredient = f.readline().strip().split(' | ')
                ingredients = {'ingredient_name': ingredient[0], 'quantity': int(ingredient[1]), 'measure': ingredient[2]}
                list_of_ingredients.append(ingredients)
            cook_book.update({dish_name: list_of_ingredients})         
            f.readline()


# cook_book = {
#   'Омлет': [
#     {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
#     {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
#     {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
#     ],
#   'Утка по-пекински': [
#     {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
#     {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
#     {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
#     {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
#     ],
#   'Запеченный картофель': [
#     {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
#     {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
#     {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
#     ]
#   }
# {
#     'Говядина': {'ingredient_name': 'Говядина', 'quantity': 1000, 'measure': 'г'}, 
#     'Перец сладкий': {'ingredient_name': 'Перец сладкий', 'quantity': 2, 'measure': 'шт'}, 
#     'Лаваш': {'ingredient_name': 'Лаваш', 'quantity': 4, 'measure': 'шт'}, 
#     'Винный уксус': {'ingredient_name': 'Винный уксус', 'quantity': 2, 'measure': 'ст.л'}, 
#     'Помидор': {'ingredient_name': 'Помидор', 'quantity': 8, 'measure': 'шт'}, 
#     'Яйцо': {'ingredient_name': 'Яйцо', 'quantity': 4, 'measure': 'шт'}, 
#     'Молоко': {'ingredient_name': 'Молоко', 'quantity': 200, 'measure': 'мл'}
#    }

# {
#   'Картофель': {'measure': 'кг', 'quantity': 2},
#   'Молоко': {'measure': 'мл', 'quantity': 200},
#   'Помидор': {'measure': 'шт', 'quantity': 4},
#   'Сыр гауда': {'measure': 'г', 'quantity': 200},
#   'Яйцо': {'measure': 'шт', 'quantity': 4},
#   'Чеснок': {'measure': 'зубч', 'quantity': 6}
# }

# {
#     'Говядина': {'quantity': 1000, 'measure': 'г'}, 
#     'Перец сладкий': {'quantity': 2, 'measure': 'шт'}, 
#     'Лаваш': {'quantity': 4, 'measure': 'шт'}, 
#     'Винный уксус': {'quantity': 2, 'measure': 'ст.л'}, 
#     'Помидор': {'quantity': 8, 'measure': 'шт'}, 
#     'Яйцо': {'quantity': 4, 'measure': 'шт'}, 
#     'Молоко': {'quantity': 200, 'measure': 'мл'}
#     }
def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            new_shop_list_item = dict(ingredient)
            new_shop_list_item['quantity'] *= person_count 
            if new_shop_list_item['ingredient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item   
                del shop_list[new_shop_list_item['ingredient_name']]['ingredient_name']
            else: 
                shop_list[new_shop_list_item['ingredient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list


get_cook_book()
book = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
print(book)

