sus = input()
def to_int(x: str):
    try:
        return int(x)
    except:
        return None
def int_from_roman_numeral(x: str):
    """
    Convert x from roman numeral to int
    Return None if x is not a valid roman numeral
    """
    thousands = ['M', 'MM', 'MMM']
    hundreds = ['C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    tens = ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    ones = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']

    x = x.upper().strip()

    total = 0
    num = None
    value = None

    for i in range(len(thousands)):
        n = thousands[i]
        v = 1000 * (i + 1)
        try:
            if x.index(n) == 0:
                num = n
                value = v
        except:
            pass
    if num is not None:
        total += value
        x = x[len(num):]

    num = None
    value = None

    for i in range(len(hundreds)):
        n = hundreds[i]
        v = 100 * (i + 1)
        try:
            if x.index(n) == 0:
                num = n
                value = v
        except:
            pass
    if num is not None:
        total += value
        x = x[len(num):]

    num = None
    value = None

    for i in range(len(tens)):
        n = tens[i]
        v = 10 * (i + 1)
        try:
            if x.index(n) == 0:
                num = n
                value = v
        except:
            pass
    if num is not None:
        total += value
        x = x[len(num):]

    num = None
    value = None

    for i in range(len(ones)):
        n = ones[i]
        v = (i + 1)
        try:
            if x.index(n) == 0:
                num = n
                value = v
        except:
            pass
    if num is not None:
        total += value
        x = x[len(num):]
    if total > 0:
        print(f'The Roman numeral {sus} translates to the number {total}')
        
int_from_roman_numeral(sus)