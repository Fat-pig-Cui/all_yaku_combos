table = [
    0,
    0,
    1,
    1,
    1,
    1,
    0,
    1,
    1,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
]

table_all = [
    [],
    [],
    [['七对']],
    [['七对', '断幺']],
    [['七对', '混老']],
    [['七对', '混色']],
    [],
    [['七对', '混色', '混老']],
    [['七对', '清色']],
    [['七对', '清色', '断幺']],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
]

new_table = table.copy()
new_table_all = table_all.copy()

print(new_table)


fans_all = [
    [['立直'], ['河底'], ['自摸']],
    [['两立'], ['立直', '一发'], ['立直', '河底'], ['立直', '自摸'], ['海底', '自摸']],
    [['两立', '一发'], ['两立', '河底'], ['两立', '自摸'], ['立直', '一发', '自摸'], ['立直', '海底', '自摸']],
    [['两立', '一发', '自摸'], ['两立', '海底', '自摸'], ['立直', '一发', '海底', '自摸']],
]

# print(new_table_all)

fans = [1, 2, 3, 4]
times = [3, 5, 5, 3]

for fan in fans:
    for time in range(times[fan - 1]):

        for i in range(len(table) - fan):
            new_table[i + fan] += table[i]
            for j in range(table[i]):
                if fans_all[fan - 1][time] + table_all[i][j] != []:
                    new_table_all[i + fan].append(fans_all[fan - 1][time] + table_all[i][j])
        # print(new_table_all)
        print(new_table)

print("=========================")
#
# fake_fans_all = [
#     [],
#     [['岭上', '自摸']],
#     [['立直', '岭上', '自摸']],
#     [['两立', '岭上', '自摸']],
# ]
# fake_new_table = []
# for i in range(len(table)):
#     fake_new_table.append(0)
# fake_times = [0, 1, 1, 1]
# fake_table_all = []
# for i in range(len(table_all)):
#     fake_table_all.append([])
#
# for fan in fans:
#     for time in range(fake_times[fan - 1]):
#
#         for i in range(len(table) - fan):
#             fake_new_table[i + fan] += table[i]
#             for j in range(table[i]):
#                 if fake_fans_all[fan - 1][time] + table_all[i][j] != []:
#                     fake_table_all[i + fan].append(fake_fans_all[fan - 1][time] + table_all[i][j])
#         # print(new_table_all)
#         print(fake_new_table)
#
# print(fake_table_all)

print(sum(new_table))
