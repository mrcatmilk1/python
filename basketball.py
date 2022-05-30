print(10 % 2)

igloo = list(map(int, input().split()))
polar = list(map(int, input().split()))
empty = []
carry = 0

if len(igloo) < len(polar):
    temperature = igloo
    igloo = polar
    polar = temperature

for i in range(len(polar)):
    temperature = igloo[i] + polar[i] + carry
    carry = temperature // 10
    empty.append(temperature % 10)

for i in range(len(polar), len(igloo)):
    temperature = igloo[1] + polar[1] + carry
    carry = temperature // 10
    empty.append(temperature % 10)
    
if carry:
    empty.append(carry)
print(empty)