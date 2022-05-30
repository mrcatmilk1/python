# msg, every letter is moved up by the length of the message + 1, and then the message is reversed
from termcolor import colored

mess = input().lower()
message = list(mess)
i = 0
total = []
while i < len(message):
    if "a" == message[i]:
        message[i] = 1 + i
    if "b" == message[i]:
        message[i] = 2 + i
    if "c" == message[i]:
        message[i] = 3 + i
    if "d" == message[i]:
        message[i] = 4 + i
    if "e" == message[i]:
        message[i] = 5 + i
    if "f" == message[i]:
        message[i] = 6 + i
    if "g" == message[i]:
        message[i] = 7 + i
    if "h" == message[i]:
        message[i] = 8 + i
    if "i" == message[i]:
        message[i] = 9 + i
    if "j" == message[i]:
        message[i] = 10 + i
    if "k" == message[i]:
        message[i] = 11 + i
    if "l" == message[i]:
        message[i] = 12 + i
    if "m" == message[i]:
        message[i] = 13 + i
    if "n" == message[i]:
        message[i] = 14 + i
    if "o" == message[i]:
        message[i] = 15 + i
    if "p" == message[i]:
        message[i] = 16 + i
    if "q" == message[i]:
        message[i] = 17 + i
    if "r" == message[i]:
        message[i] = 18 + i
    if "s" == message[i]:
        message[i] = 19 + i
    if "t" == message[i]:
        message[i] = 20 + i
    if "u" == message[i]:
        message[i] = 21 + i
    if "v" == message[i]:
        message[i] = 22 + i
    if "w" == message[i]:
        message[i] = 23 + i
    if "x" == message[i]:
        message[i] = 24 + i
    if "y" == message[i]:
        message[i] = 25 + i
    if "z" == message[i]:
        message[i] = 26 + i
    if " " == message[i]:
        message[i] = 0
    message[i] = message[i] * len(mess)
    for num in str(message[i]):
        if message[i] < 27:
            pass
        else:
            message[i] = int(message[i]) % 26
    total.append(message[i])
    i += 1
n = 0
final = []
while n < len(total):
    if 1 == total[n]:
        total[n] = "a"
    if 2 == total[n]:
        total[n] = "b"
    if 3 == total[n]:
        total[n] = "c"
    if 4 == total[n]:
        total[n] = "d"
    if 5 == total[n]:
        total[n] = "e"
    if 6 == total[n]:
        total[n] = "f"
    if 7 == total[n]:
        total[n] = "g"
    if 8 == total[n]:
        total[n] = "h"
    if 9 == total[n]:
        total[n] = "i"
    if 10 == total[n]:
        total[n] = "j"
    if 11 == total[n]:
        total[n] = "k"
    if 12 == total[n]:
        total[n] = "l"
    if 13 == total[n]:
        total[n] = "m"
    if 14 == total[n]:
        total[n] = "n"
    if 15 == total[n]:
        total[n] = "o"
    if 16 == total[n]:
        total[n] = "p"
    if 17 == total[n]:
        total[n] = "q"
    if 18 == total[n]:
        total[n] = "r"
    if 19 == total[n]:
        total[n] = "s"
    if 20 == total[n]:
        total[n] = "t"
    if 21 == total[n]:
        total[n] = "u"
    if 22 == total[n]:
        total[n] = "v"
    if 23 == total[n]:
        total[n] = "w"
    if 24 == total[n]:
        total[n] = "x"
    if 25 == total[n]:
        total[n] = "y"
    if 26 == total[n]:
        total[n] = "z"
    if 0 == total[n]:
        total[n] = " "
    final.append(total[n])
    n += 1
final.reverse()
output = ""
for f in final:
    output += f
print(colored(output, 'red'))