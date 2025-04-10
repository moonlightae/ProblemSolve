# L = int(input())
# s = [64]
# while True:
#     if sum(s) != L:
#         if sum(s) > L:
#             a = s.pop(s.index(min(s)))
#             if a//2 != 0:
#                 s.append(a//2)
#                 s.append(a//2)
#             if sum(s) - a//2 >= L and a//2 != 0:
#                 s.pop()
#     else:
#         print(len(s))
#         break

print(bin(int(input()))[2:].count('1'))