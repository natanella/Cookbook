from pprint import pprint

def add_recipe(name, *ingredients):
    recipe = f"{name}\n{len(ingredients)}\n"
    for ingredient in ingredients:
        recipe += f"{' | '.join(ingredient.split(','))}\n"

    with open('recipes.txt', encoding='utf-8') as f:
        data = f.read()
        if not data:
            with open('recipes.txt', 'w', encoding='utf-8') as f:
                f.write(recipe)
        else:
            with open('recipes.txt', 'a', encoding='utf-8') as f:
                f.write(f"\n{recipe}")

def read_cookbook():
    cookbook = {}
    with open('recipes.txt', encoding='utf-8') as f:
        recipes = f.read().split('\n\n')

        for r in recipes:
            name = r.split('\n')[0]
            ingredients = []
            count = int(r.split('\n')[1])

            for el in r.split('\n')[2:count+2]:
                ing = {
                    'ingredient_name': el.split(' | ')[0],
                    'quantity': el.split(' | ')[1],
                    'measure': el.split(' | ')[2]
                }
                ingredients.append(ing)

            cookbook[name] = ingredients

    return cookbook

def get_shop_list_by_dishes(dishes, person_count):
    cookbook = read_cookbook()
    shop_list = {}

    for dish in dishes:
        for ingredient in cookbook[dish]:
            shop_list[ingredient['ingredient_name']] = {
                'measure': ingredient['measure'],
                'quantity': int(ingredient['quantity']) * person_count
            }
    pprint(shop_list)

add_recipe('Омлет', 'Яйцо,2,шт', 'Молоко,100,мл', 'Помидор,2,шт')
add_recipe('Утка по-пекински', 'Утка,1,шт', 'Вода,2,л', 'Мед,3,ст.л', 'Соевый соус,60,мл')
add_recipe('Запеченный картофель', 'Картофель,1,кг', 'Чеснок,3,зубч', 'Сыр гауда,100,г')
add_recipe('Фахитос', 'Говядина,500,г', 'Перец сладкий,1,шт', 'Лаваш,2,шт', 'Винный уксус,1,ст.л', 'Помидор,2,шт')
        
pprint(read_cookbook())
    
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)