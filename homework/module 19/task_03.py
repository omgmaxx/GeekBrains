data = {
    "address": "0x544444444444",
    "ETH": {
        "balance": 444,
        "totalIn": 444,
        "totalOut": 4
    },
    "count_txs": 2,
    "tokens": [
        {
            "fst_token_info": {
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False
            },
            "balance": 5000,
            "totalIn": 0,
            "total_out": 0
        },
        {
            "sec_token_info": {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuances_count": 0,
                "holders_count": 20707,
                "price": False
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 0
        }
    ]
}
print('Ключи: ')                                                                                        # Вывести списки ключей и значений словаря.
for x in data.keys():
    print('--', x)
print('Значения: ')
for y in data.values():
    print('--', y)

data['ETH'].update({'total_diff': 100})                                                                 # В “ETH” добавить ключ “total_diff” со значением 100.

data['tokens'][0]['fst_token_info'].update({'name': 'doge'})                                            # Внутри “fst_token_info” значение ключа “name”
                                                                                                        # поменять с “fdf” на “doge”.

data['ETH'].update({'totalOut': data['tokens'][0].pop('total_out')})                                    # Удалить “total_out” из tokens и присвоить
data['tokens'][1].pop('total_out')                                                                      # его значение в “total_out” внутри “ETH”.

data['tokens'][1]['sec_token_info']['total_price'] = data['tokens'][1]['sec_token_info'].pop('price')   # Внутри "sec_token_info" изменить название
                                                                                                        # ключа “price” на “total_price”.

# for a in data:
#     if a == 'ETH':
#         print(f'{a}:')
#         for b in data[a]:
#             print(f'-- {b}: {data[a].get(b)}')
#     elif a == 'tokens':
#         print(f'{a}:')
#         for x in range(2):
#             print('=======')
#             for b in data[a][x]:
#                 if b == 'fst_token_info' or b == 'sec_token_info':
#                     print(f'-- {b}:')
#                     for c in data[a][x][b]:
#                         print(f'---- {c}: {data[a][x][b].get(c)}')
#                 else:
#                     print(f'-- {b}: {data[a][x].get(b)}')
#     else:                                                                                             # Возможно, я не очень понял первое
#         print(f'{a}: {data.get(a)}')                                                                  # задание - так что вот запасной вариант


