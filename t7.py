'''
x[0] = 2016 | 1958
x[1] = 2000 | 1995 | 2015
x[2] = 1963 | 1995 | 1964
x[3] = 1958 | 2002 | 1997
x[4] = 1989 | 2010 | 1985
'''


def main(x):
    y = [
        [2016, 1958].index(x[0]),
        [2000, 1995, 2015].index(x[1]),
        [1963, 1995, 1964].index(x[2]),
        [1958, 2002, 1997].index(x[3]),
        [1989, 2010, 1985].index(x[4]),
    ]
    return solve(y)


def solve(x):
    return 0


# #3?
# def main(x):
#     y = [
#         [2016, 1958].index(x[0]),
#         [2000, 1995, 2015].index(x[1]),
#         [1963, 1995, 1964].index(x[2]),
#         [1958, 2002, 1997].index(x[3]),
#         [1989, 2010, 1985].index(x[4]),
#     ]
#
#     match y:
#         case [_, _, 1, _, _]:
#             return 12
#         case [_, _, 2, _, _]:
#             return 13
#         case [_, 1, 0, _, _]:
#             return 6
#         case [_, 0, 0, 1, _]:
#             return 2
#
#         case [_, 0, 0, 0, _]:
#             return y[0]
#         case [_, 0, 0, 2, _]:
#             return 3+y[4]
#
#         case [_, 2, 0, 2, _]:
#             return 11
#         case [_, 2, 0, 0, _]:
#             return 7 + y[0]
#         case [_, 2, 0, 1, _]:
#             return 9 + y[0]
#
#     return y

# #3
# def main(x):
#     match x[2]:
#         case 1995:
#             return 12
#         case 1964:
#             return 13
#         case _:
#             return layer_1(x)
#
#
# def layer_1(x):
#     match x[1]:
#         case 1995:
#             return 6
#         case 2000:
#             return layer_1_1(x)
#         case _:
#             return layer_1_2(x)
#
#
# def layer_1_1(x):
#     match x[3]:
#         case 2002:
#             return 2
#         case 1958:
#             return layer_1_1_1(x)
#         case _:
#             return layer_1_1_2(x)
#
#
# def layer_1_1_1(x):
#     match x[0]:
#         case 2016:
#             return 0
#         case _:
#             return 1
#
#
# def layer_1_1_2(x):
#     match x[4]:
#         case 1989:
#             return 3
#         case 2010:
#             return 4
#         case _:
#             return 5
#
#
# def layer_1_2(x):
#     match x[3]:
#         case 1997:
#             return 11
#         case 1958:
#             return layer_1_2_1(x)
#         case _:
#             return layer_1_2_2(x)
#
#
# def layer_1_2_1(x):
#     match x[0]:
#         case 2016:
#             return 7
#         case _:
#             return 8
#
#
# def layer_1_2_2(x):
#     match x[0]:
#         case 2016:
#             return 9
#         case _:
#             return 10


# #2
# def main(x):
#     year = x[2]
#     switcher = {
#         1995: 12,
#         1964: 13
#     }
#     return switcher.get(year, layer_1(x))
#
#
# def layer_1(x):
#     year = x[1]
#     switcher = {
#         1995: 6,
#         2000: layer_1_1(x)
#     }
#     return switcher.get(year, layer_1_2(x))
#
#
# def layer_1_1(x):
#     year = x[3]
#     switcher = {
#         2002: 2,
#         1958: layer_1_1_1(x)
#     }
#     return switcher.get(year, layer_1_1_2(x))
#
#
# def layer_1_1_1(x):
#     year = x[0]
#     switcher = {
#         2016: 0
#     }
#     return switcher.get(year, 1)
#
#
# def layer_1_1_2(x):
#     year = x[4]
#     switcher = {
#         1989: 3,
#         2010: 4
#     }
#     return switcher.get(year, 5)
#
#
# def layer_1_2(x):
#     year = x[3]
#     switcher = {
#         1997: 11,
#         1958: layer_1_2_1(x)
#     }
#     return switcher.get(year, layer_1_2_2(x))
#
#
# def layer_1_2_1(x):
#     year = x[0]
#     switcher = {
#         2016: 7
#     }
#     return switcher.get(year, 8)
#
#
# def layer_1_2_2(x):
#     year = x[0]
#     switcher = {
#         2016: 9
#     }
#     return switcher.get(year, 10)


# #1
# def main(x):
#     if x[2] == 1995:
#         return 12
#     elif x[2] == 1964:
#         return 13
#     else:
#         return layer_1(x)
#
#
# def layer_1(x):
#     if x[1] == 1995:
#         return 6
#     elif x[1] == 2000:
#         return layer_1_1(x)
#     else:
#         return layer_1_2(x)
#
#
# def layer_1_1(x):
#     if x[3] == 2002:
#         return 2
#     elif x[3] == 1958:
#         return layer_1_1_1(x)
#     else:
#         return layer_1_1_2(x)
#
#
# def layer_1_1_1(x):
#     if x[0] == 2016:
#         return 0
#     else:
#         return 1
#
#
# def layer_1_1_2(x):
#     if x[4] == 1989:
#         return 3
#     elif x[4] == 2010:
#         return 4
#     else:
#         return 5
#
#
# def layer_1_2(x):
#     if x[3] == 1997:
#         return 11
#     elif x[3] == 1958:
#         return layer_1_2_1(x)
#     else:
#         return layer_1_2_2(x)
#
#
# def layer_1_2_1(x):
#     if x[0] == 2016:
#         return 7
#     else:
#         return 8
#
#
# def layer_1_2_2(x):
#     if x[0] == 2016:
#         return 9
#     else:
#         return 10

print("Expected 12, Got:", main([1958, 1995, 1995, 1958, 1985]))
print("Expected 13, Got:", main([1958, 1995, 1964, 1958, 1989]))
print("Expected 8, Got:", main([1958, 2015, 1963, 1958, 1985]))
print("Expected 0, Got:", main([2016, 2000, 1963, 1958, 2010]))
print("Expected 9, Got:", main([2016, 2015, 1963, 2002, 1985]))
