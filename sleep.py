def works(value: int, records: list):
    current = 0
    for r in records:
        current += r
        if current > value:
            return False
        elif current == value:
            current = 0
    return current == 0

def solve(records: list) -> int:
    n = len(records)
    total = sum(records)
    for i in range(n, 1, -1):
        if total % i != 0:
            continue
        value = total // i
        if works(value, records):
            return n - i
    return n - 1

t = int(input())
for _ in range(t):
    n = int(input())
    records = list(map(int, input().split()))
    print(solve(records))