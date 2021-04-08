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

def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print(f"{shop_list_item['ingredient_name']} {shop_list_item['quantity']} {shop_list_item['measure']}")

def create_shop_list():
    person_count = int(input('Введите количество персон: '))
    dishes = input('Введите блюда через запятую: ').split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            new_shop_list_item = dict(ingredient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingredient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingredient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list


get_cook_book()
create_shop_list()
