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

