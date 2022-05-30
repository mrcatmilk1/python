operators = {
    "+": lambda num1, num2: num1 + num2,
    "-": lambda num1, num2: num1 - num2,
    "*": lambda num1, num2: num1 * num2,
    "/": lambda num1, num2: num1 / num2,   
}


def parse_num(word: str):
    """
    Parses an integer at the front of `word`.

    #### Arguments
    - `word`: The string to be parsed.

    ##### Return
    - `num`, `substring`: The int that has been parsed and the remaining substring. `num` is `None` if there is no `int` prefix. `substring` can be `None` if the whole string is an `int` representation.
    """
    word = word.strip()
    i = 0
    while i < len(word) and  not word[i].isnumeric():
        i += 1
    
    if i == len(word):
        return None, word
    
    num = 0
    while i < len(word) and word[i].isnumeric():
        num *= 10
        num += int(word[i])
        i += 1

    if i == len(word):
        return num, None
    
    return num, word[i:].strip()


def parse_operator(word: str):
    """
    Parses an operator at the front of `word`.

    #### Arguments
    - `word`: The string to be parsed.

    ##### Return
    TODO: fix
    - `operator`, `substring`: The int that has been parsed and the remaining substring. `num` is `None` if there is no `int` prefix. `substring` can be `None` if the whole string is an `int` representation.
    """
    word = word.strip()
    if not word:
        return None, None
    c = word[0]
    if c not in operators:
        return None, word
    word = word[1:]
    if not word:
        return c, None
    return c, word.strip()



line = input("Expression: ")

try:
    num1, line = parse_num(line)
    operator, line = parse_operator(line)    
    num2, _ = parse_num(line)
    print(num2)
    print(line)
    result = operators[operator](num1, num2)
    print(f"{num1} {operator} {num2} = {result}")
except:
    print("Error while perfoming opertion.")


# if '.' in num1 or '.' in num2:
#     if op == '+':
#         print(float(num1) + float(num2))
#     if op == '-':
#         print(float(num1) - float(num2))
#     if op == '*':
#         print(float(num1) * float(num2))
#     if op == '/':
#         print(float(num1) / float(num2))
#     if op == '**':
#         print(float(num1) ** float(num2))
#     if op == '//':
#         print(float(num1) // float(num2))
#     if op == '%':
#         print(float(num1) % float(num2))
# else:
#     if op == '+':
#         print(int(num1) + int(num2))
#     if op == '-':
#         print(int(num1) - int(num2))
#     if op == '*':
#         print(int(num1) * int(num2))
#     if op == '/':
#         print(int(num1) / int(num2))
#     if op == '**':
#         print(int(num1) ** int(num2))
#     if op == '//':
#         print(int(num1) // int(num2))
#     if op == '%':
#         print(int(num1) % int(num2))






























































































































































