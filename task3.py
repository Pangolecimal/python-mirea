from functools import reduce


def main(n, a, m, p):
    return reduce(
        lambda acc_i, i: acc_i + reduce(
            lambda acc_j, j: acc_j + reduce(
                lambda acc_k, k: acc_k + 68 * (
                    34*i)**2 - (k**2 + 37 + p**3)**5 - j,
                range(1, n + 1),
                0
            ),
            range(1, a + 1),
            0
        ),
        range(1, m + 1),
        0
    )


# def main(n, a, m, p):
#     result = 0
#     for i in range(1, m+1):
#         for j in range(1, a+1):
#             for k in range(1, n+1):
#                 result += 68 * (34*i)**2 - (k**2 + 37 + p**3)**5 - j
#     return result

print(main(6, 4, 8, -0.07))
