"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух) разной!! сложности
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""

import heapq, operator

companies = {'Horns and Hoofs': 9000, 'Skull and Bones': 15000, 'Today and Tomorrow': 3500, 'Cloak and Dagger': 11000, 'Infinity and Beyond': 23700}

#Способ 1       #O(n)
print(heapq.nlargest(3, companies.items(), key=operator.itemgetter(1)))     #O(n)

#Способ 2       #O(n log n)
list_companies = list(companies.items())            #O(n)
list_companies.sort(key = lambda i : i[1])          #O(n log n)
print(list_companies[2:])                           #O(b-a)

#Способ 3       #O(n^2)
def keywithmaxval(c):
    k = sorted(c.values())[::-1]                    #O(n log n)
    return k[:3]

for key in companies.keys():                        #O(n)
    if companies[key] in keywithmaxval(companies):  #O(n)
        print(key, companies[key])                  #O(1)

#Вывод: из всех решений способ 1 является наиболее оптимальным как по сложности О, так и по лаконичности кода. Самым худшим является способ 3.
