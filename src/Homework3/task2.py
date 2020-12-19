'''
List practice
1. Используйте генератор списков чтобы получить следующий:
    ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
2. Используйте на предыдущий список slice чтобы получить следующий:
    ['ab', 'ad', 'bc'].
3. Используйте генератор списков чтобы получить следующий
    ['1a', '2a', '3a', '4a'].
4. Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.

5. Скопируйте список и добавьте в него элемент '2a'
    так чтобы в исходном списке этого элемента не было.
'''
list_1 = [a + i for a in 'ab' for i in 'bcd']
print(list_1)

list_2 = list_1[::2]
print(list_2)

list_3 = [str(i) + 'a' for i in range(1,5)]
print(list_3)

print(list_3.pop(1), list_3)

list_5 = list_3[:]
list_5.insert(1, '2a')
print(list_3, list_5)
