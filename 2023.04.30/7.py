list_of_dicts = [
    {
        'Липецк': 1,
        'Пермь': 9,
        'Ростов-на-Дону': 6,
        'Тула': 3,
        'Ульяновск': 7,
        'Ярославль': 9
    },
    {
        'Барнаул': 5,
        'Краснодар': 9,
        'Красноярск': 9,
        'Махачкала': 5,
        'Новосибирск': 7,
        'Пермь': 3,
        'Ростов-на-Дону': 5,
        'Самара': 2,
        'Санкт-Петербург': 6,
        'Хабаровск': 7
    },
    {
        'Краснодар': 4,
        'Красноярск': 1,
        'Москва': 1,
        'Санкт-Петербург': 4,
        'Тольятти': 9,
        'Тула': 2,
        'Тюмень': 5,
        'Ульяновск': 4
    },
]

list_out = {}

for city in list_of_dicts:
    for name, v in city.items():
        # ИСПРАВИТЬ: используйте словарные методы вместо явной проверки наличия ключа в словаре
        if name in list_out:
            list_out[name] = list_out[name] | {v}
        else:
            list_out[name] = {v}

print(*{
    # ИСПОЛЬЗОВАТЬ: есть синтаксис f-строк для машиночитаемого строкового представления:
    f'{k!r}: {v}'
    for k, v in list_out.items()
}, sep=',\n')

# ИСПОЛЬЗОВАТЬ: альтернативный "однострочник" — не стоит писать такой код в реальной жизни, но для тренировки очень даже хорошо =)
# from itertools import chain
# print(*{
#     f'{city!r}: { {dict_.get(city) for dict_ in list_of_dicts} - {None} }'
#     for city in set(chain(*list_of_dicts))
# }, sep=',\n')


# 'Махачкала': {5},
# 'Ростов-на-Дону': {5, 6},
# 'Ульяновск': {4, 7},
# 'Краснодар': {9, 4},
# 'Тольятти': {9},
# 'Ярославль': {9},
# 'Тула': {2, 3},
# 'Хабаровск': {7},
# 'Москва': {1},
# 'Пермь': {9, 3},
# 'Барнаул': {5},
# 'Самара': {2},
# 'Тюмень': {5},
# 'Новосибирск': {7},
# 'Красноярск': {9, 1},
# 'Липецк': {1},
# 'Санкт-Петербург': {4, 6}


# ИТОГ: хорошо, но можно лучше — 3/4
