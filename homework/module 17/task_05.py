word = str(input('Введите строку: '))

h_List = [x for x in range(len(word)) if word[x] == 'h']

print(f'Развёрнутая последовательность между первым и последним h: {word[ (h_List[-1] - 1) : h_List[0] : -1 ]}.')
