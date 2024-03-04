import math


# Этот код не проходит по сложности
# def main(P):
#     A = []
#     for p in P:
#         if p < 86 and p >= -52:
#             A.append(math.floor(p/8)+abs(p))
#
#     S = []
#     for a in A:
#         if a < -54 or a > 40:
#             S.append(abs(a))
#
#     F = []
#     for p in P:
#         for a in A:
#             if p < a:
#                 F.append((p % 2)+a*a)
#
#     tau = sum(abs(f) for f in F) + sum(f*s for f in F for s in S)
#
#     return tau


# А этот прошёл... как?
def main(P):
    A = {math.floor(p/8)+abs(p) for p in P if (p >= -52 and p < 86)}
    S = {abs(a) for a in A if (a < -54 or a > 40)}
    F = {(p % 2)+a*a for p in P for a in A if (p < a)}
    tau = sum(abs(f) for f in F) + sum(f*s for f in F for s in S)
    return tau


print("Expect: 1218992   Got:", main(
    {97, 43, -52, -77, -43, 90, -69, -98, -33}))
print("Expect: 22616613   Got:", main(
    {40, 76, -51, 80, 52, -7, 26, 61, 25, -97}))
