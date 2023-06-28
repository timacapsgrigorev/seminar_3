# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

elements = [1, 2, 3, 3, 4, 5, 5, 5, 5, 6, 6, 6]
new_elements = []
for element in elements:
    elem_in = elements.count(element)
    if elem_in > 1:
        new_elements.append(element)
new_elements = (set(new_elements))
print(list(new_elements))