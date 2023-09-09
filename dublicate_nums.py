def dublicate_n(lst):
    return list(set([i for i in lst
                     if lst.count(i) > 0]))     # 0 для вывода всего списка


lst = [1, 3, 3, 4, 4, 2, 1, 4, 4, 2, 1, 5]
print(dublicate_n(lst))
