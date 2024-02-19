# #4
def main(n):
    res = [0.52, -0.47] + [0] * (n+1)
    res = [(res[i]=res[i] if i < 2 else res[i-1] ** 2 - 1 - res[
        i-2] ** 3) for i, v in enumerate(res)]
    print(res)
    return res[n]


#
# def f(n):
#     return main(n-1) ** 2 - 1 - main(n-2) ** 3

# def main(n):
#     res = {0: 0.52, 1: -0.47}
#     i = 2
#     while i <= n:
#         res.update({i: res.get(i-1) ** 2 - 1 - res.get(i-2) ** 3})
#         i += 1
#     return res[n]

# #3
# def main(n):
#     a, b = 0.52, -0.47
#     for i in range(2, n+1):
#         a, b = b, b ** 2 - 1 - a ** 3
#     return b


# #2
# def main(n):
#     res = [0.52, -0.47]
#     for i in range(2, n+1):
#         res.append(res[i-1] ** 2 - 1 - res[i-2] ** 3)
#     return res[n]


# #5
# def main(n):
#     return 0.52 if n == 0 else -0.47 if n == 1 else main(
#         n-1) ** 2 - 1 - main(n-2) ** 3


#  #1
# def main(n):
#     if n == 0:
#         return 0.52
#     elif n == 1:
#         return -0.47
#     else:
#         return main(n-1) ** 2 - 1 - main(n-2) ** 3
print(main(8))
