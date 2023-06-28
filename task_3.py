# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# Верните все возможные варианты комплектации рюкзака.


def find_items_backpack(items, max_weight):
    backpack = {}
    current_weight = 0

    sorted_items = sorted(items.items(), key=lambda x: x[1], reverse=True)

    for item, weight in sorted_items:
        if current_weight + weight <= max_weight:
            backpack[item] = weight
            current_weight += weight

    return backpack

items = {
    'Палатка': 2.5,
    'Спальный мешок': 1.8,
    'Каремат': 0.7,
    'Котелок': 0.5,
    'Фонарик': 0.3,
    'Печка': 3.2,
    'Посуда': 1.0
}
max_weight = 7.0

backpack_contents = find_items_backpack(items, max_weight)

print("Вещи в рюкзаке:")
for item, weight in backpack_contents.items():
    print(f"{item} ({weight} кг)")