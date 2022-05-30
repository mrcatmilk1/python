print("Converts the number from decimal to the given base using the symbols provided.")

num = int(input("Number: "))
base = int(input("Base: "))
symbols = input("Symbols: ").split()

if len(symbols) == 0:
    symbols = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

remain = []
while num != 0:
    remain.append(num % base)
    num = num // base


print("".join(map(lambda x: symbols[x], reversed(remain))))
