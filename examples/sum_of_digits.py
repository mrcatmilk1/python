# Given a number, find the sum of digits in the number

# 10303003030458383 = ....

# 1 + 3 + 3 + 3 + 3 + 4 + 5 + 8 + 3 + 8 + 3
number = int(input("Number: "))
piece = number

sum = 0

while piece != 0:
    e = piece % 10
    sum += e
    piece = piece // 10
print(sum)

