cook_book = {}
key = ['ingredient_name', 'quantity', 'measure']
with open('recipes.txt', 'r', encoding='utf-8') as f:
    for line in f:
        dush_name = line.strip()
        counter = int(f.readline().strip())
        ingredients = []
        for i in range(counter):
            q = f.readline().strip().split(' | ')
            ingredients.append(dict(zip(key, q)))
            cook_book[dush_name] = ingredients
        f.readline()
    # print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    a = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            a[ingredient.get('ingredient_name')] = {'measure': ingredient.get('measure'), 'quantity': int(ingredient.get('quantity')) * person_count}
    print(a)
    return

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
