# def Foctoryal(x):
#     summ = 1
#     for i in range(1, x + 1):
#         summ *= i # 1 * 2 * 3 * 4 * 5
#     return summ
# print(Foctoryal(5))
#
# def Fobanaci(x):
#     f1 = f2 = 1
#     print(f1, f2, end=' ')
#     for i in range(2,x + 1):
#         f1, f2 = f2, f2 + f1 # 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597
#         print(f2, end=' ')
#
# Fobanaci(1000)def
# def Summ_info(*args, **kwargs):
#     return args, kwargs
# print(Summ_info(1,3,23,2323,23,name='Samandar',age=12, group=817))
#
# user = {
#     'Islombek':1,
#     'Lola': 2,
#     # 'Munisa': 3,
#     # # 'Abdulaziz': 4,
#     # # 'Samandar': 5,
#     # # 'bexruz': 6
# }
# baxolar = {
#     1:{
#         'IT': 5,
#         'Matem':5,
#         'Ingliz':5,
#         'Bio':4
#     },
#     2:{
#         'IT': 5,
#         'Matem':5,
#         'Ingliz':5,
#         'Bio':5
#     },
#     # 3:{
#     #     'IT': 5,
#     #     'Matem':5,
#     #     'Ingliz':5,
#     #     'Bio':5
#     # },
#     # # 4:{
#     # #     'IT': 5,
#     # #     'Matem':2.4,
#     # #     'Ingliz':5,
#     # #     'Bio':5
#     # # },
#     # # 5:{
#     # #     'IT': 4,
#     # #     'Matem':4,
#     # #     'Ingliz':4,
#     # #     'Bio':4
#     # # },
#     # # 6:{
#     # #     'IT': 5,
#     # #     'Matem':3,
#     # #     'Ingliz':5,
#     # #     'Bio':4
#     # # }
#
# }
# for ism, ism_id in user.items():
#     print(ism_id)
#     umumuy = 0
#     for fan, baxo in baxolar[ism_id].items():
#         umumuy += baxo
#     print(f'Isim: {ism}\nUmumiy Baxo {umumuy}\nYakuniy {round(umumuy/4, 2)}')
def Juft(son):
    if son % 2 ==0:
        return "JUFT"
    else:
        return "TOQ"

#############################

while True:
    son = int(input("Son:"))
    print(Juft(son))
