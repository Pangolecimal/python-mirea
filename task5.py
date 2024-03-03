from math import acos, ceil


def main(z, y, x, i=1, s=0):
    if i == len(x)+1:
        return (1/43) * s

    n = len(x)

    return main(z, y, x, i + 1, s + acos(z[n-ceil(i/4)] ** 3 +
                                         y[n-ceil(i/4)] ** 2 +
                                         x[n-i]) ** 5)

# def main(z, y, x):
#     n = len(y)
#     sum = 0
#     i = 1
#     while i <= n:
#         sum += (1/43) * acos(z[n-ceil(i/4)] ** 3 +
#                              y[n-ceil(i/4)] ** 2 +
#                              x[n-i]) ** 5
#         i += 1
#     return sum

# def main(z, y, x):
#     n = len(x)
#     return sum((1/43) * acos(z[n-ceil(i/4)] ** 3 +
#                              y[n-ceil(i/4)] ** 2 +
#                              x[n-i]) ** 5 for i in range(1, n+1))


# def main(z, y, x):
#     n = len(x)
#     sum = 0
#     for i in range(1, n + 1):
#         sum += (1/43) * acos(z[n-ceil(i/4)] ** 3 +
#                              y[n-ceil(i/4)] ** 2 +
#                              x[n-i]) ** 5
#     return sum


print(main([-0.31, -0.36, -1.0, -0.62, -0.32, -0.08, 0.33],
           [0.6, -0.1, -0.12, -0.15, -0.79, 0.09, -0.56],
           [-0.76, -0.82, 0.71, 0.3, -0.85, -0.91, 0.46]))
