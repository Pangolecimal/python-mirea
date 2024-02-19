

# def all_permutations(s):
#     if len(s) == 0:
#         return ['']
#
#     permutations = []
#     for i in range(len(s)):
#         rest = s[:i] + s[i+1:]
#         for p in all_permutations(rest):
#             permutations.append(s[i] + p)
#
#     return permutations
#
#
# # Example usage:
# string = "abc"
# result = all_permutations(string)
# print(result)
#

# import math
# import tkinter as tk
#
#
# def draw(shader, width, height):
#     image = bytearray((0, 0, 0) * width * height)
#     for y in range(height):
#         for x in range(width):
#             pos = (width * y + x) * 3
#             color = shader(x / width, y / height)
#             normalized = [max(min(int(c * 255), 255), 0) for c in color]
#             image[pos:pos + 3] = normalized
#     header = bytes(f'P6\n{width} {height}\n255\n', 'ascii')
#     return header + image
#
#
# def main(shader):
#     label = tk.Label()
#     img = tk.PhotoImage(data=draw(shader, 600, 600)).zoom(2, 2)
#     label.pack()
#     label.config(image=img)
#     tk.mainloop()
#
#
# def shader(x, y):
#     c1x = 0.5
#     c1y = 0.5
#     r1 = 0.3
#     c2x = 0.55
#     c2y = 0.5
#     r2 = 0.275
#     d1 = ((x-c1x) ** 2 + (y-c1y) ** 2) ** 0.5 - r1
#     d2 = ((x-c2x) ** 2 + (y-c2y) ** 2) ** 0.5 - r2
#     m = (d1 < 0 and d2 > 0)
#     return m - abs(d2)*10, -d1*2, -d2*2
#
#
# main(shader)
