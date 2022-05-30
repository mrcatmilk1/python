x, y, m = list(map(int, input().split()))
# if x > y:
#     if m % x == 0:
#         print(f'{m / x} {x}')
# if y > x:
#     if m % y == 0:
#         print(f'{m / y} {y}')
# if x > y:
#     if m % y == 0 and m % x != 0:
#         print(f'{m / y} y')
# if y > x:
#     if m % x == 0 and m % y != 0:
#         print(f'{m / x} x')
# if m % y != 0 and m % x != 0:
#     if y > x and y < m:
#         while m - y > y:
#             m = m - y
#         while m - x > 0:
#             m = m - x
#         print(f'{3 - 5}')
#     if x > y and x < m:
#         while m - x > x:
#             m = m - x
#         while m - y > 0:
#             m = m - y
#         print(f'{1 - 5}')


if y > x:
    whyy = m // y
    ex = whyy // x
    print(f'{whyy} {y} and {ex} {x}')
if x > y:
    exx = m // x
    why = exx // y
    print(f'{why} {y} and {exx} {x}')