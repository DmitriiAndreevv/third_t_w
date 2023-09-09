def my_backpack(items, back_weight):
    team_items = []
    for item, weight in items.items():
        if weight < back_weight:
            team_items.append(item)
            back_weight -= weight
    return team_items


items = {'палатка': 4, 'вода': 1, 'еда': 2, 'компас': 3, 'одежда': 1, 'удочка': 1, 'спички': 1}
back_weight = 13
print(my_backpack(items, back_weight))
