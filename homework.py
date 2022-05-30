from re import L
from termcolor import colored
num = list(map(int, input()))
i = -1
j = 0
ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
onetens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
done = []
while len(num) * -1 <= i:
    while num[i] != j:
        j += 1
    done.append(ones[j])
    j = 0
    i -= 1

o = 0
t = 2
one = ""
ten = ""

if len(num) == 1:
    one += done[0]
    print(one)

if len(num) == 2:
    if done[1] == "zero":
        one += done[0]
        print(one)
    if done[-1] == "one":
        while done[0] != ones[o]:
            o += 1
        ten += (onetens[o])
    else:
        if done[1] != "zero":
            while done[-1] != ones[t]:
                t += 1
            ten += (tens[t - 2])
            ten += " "
            ten += (done[0])
    print(ten)

hundred = ""

if len(num) == 3:
    if done[1] == "zero":
        hundred += done[-1]
        hundred += " hundred and "
        hundred += done[0]
    else:
        if done[1] == "one":
            while done[0] != ones[o]:
                o += 1
            hundred += (done[-1])
            hundred += (" hundred and ")
            hundred += (onetens[o])
        else:
            while done[1] != ones[t]:
                t += 1
            hundred += (done[-1])
            hundred += (" hundred and ")
            hundred += (tens[t - 2])
            hundred += " "
            hundred += done[0]
    print(hundred)

    thousand = ""
    if len(num) == 4:
        if done[1] == "zero":
            thousand += done[-1]
            thousand += " thousand "
            thousand += done[2]
            thousand += " hundred and "
            thousand += done[0]
        else:
            if done[1] == "one":
                while done[0] != ones[o]:
                    o += 1
                thousand += done[-1]
                thousand += " thousand "
                thousand += done[2]
                thousand += " hundred and "
                thousand += onetens[o]
            else:
                while done[1] != ones[t]:
                    t += 1
                thousand += done[-1]
                thousand += " thousand "
                thousand += done[2]
                thousand += " hundred and "
                thousand += tens[t-2]
                thousand += " "
                thousand += done[0]
    print(thousand)

ten_thousand = ""

if len(num) == 5:
    o = 0
    if done[4] == "one":
        while done[3] != ones[o]:
            o += 1
        ten_thousand += onetens[o]
        o = 0
        ten_thousand += " thousand "
        ten_thousand += done[2]
        ten_thousand += " hundred and "
        if done[1] == "one":
            while done[0] != ones[o]:
                o += 1
            ten_thousand += (onetens[o])
        else:
            while done[1] != ones[t]:
                t += 1
            ten_thousand += (tens[t - 2])
            ten_thousand += " "
            ten_thousand += done[0]
    else:
        while done[4] != ones[t]:
            t += 1
        ten_thousand += tens[t-2]
        t = 0
        ten_thousand += " "
        ten_thousand += done[3]
        ten_thousand += " thousand "
        ten_thousand += done[2]
        ten_thousand += " hundred and "
        if done[1] == "one":
            while done[0] != ones[o]:
                o += 1
            ten_thousand += (onetens[o])
        else:
            while done[1] != ones[t]:
                t += 1
            ten_thousand += (tens[t - 2])
            ten_thousand += " "
            ten_thousand += done[0]
    print(ten_thousand)

if len(num) > 5:
    print(colored("The number is too small, please type in a bigger number.", "green"))