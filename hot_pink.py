from termcolor import colored

se =  list(map(int, input().split()))
print(se)
i = 0

for j in range(1, 1000):
    while i < len(se):
        if se[i] < 300:
            se[i] += 1
            print(colored(f'who is joe {se}', 'magenta'))
        else:
            se[i] += j
            i += 1