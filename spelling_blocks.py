from typing import Set, List

n = int(input())
blocks = [set(input()) for _ in range(4)]
words = [input() for _ in range(n)]


def can_spell_with_options(options: List[Set[str]], exclude: Set[str]):

    if not options:
        return True
    
    first = options[0].copy()
    for i in exclude:
        first.discard(i)
    
    if not first:
        return False

    for opt in first:
        temp = exclude.copy()
        temp.add(opt)

        if can_spell_with_options(options[1:], temp):
            return True
    
    return False

        

def can_spell(word: str):
    """
    Return `true` if the word can be spelt using `blocks`
    """
    options = []
    for letter in word:
        current = set()
        for i in range(len(blocks)):
            if letter in blocks[i]:
                current.add(i)
        if len(current) == 0:
            return False
        options.append(current)

    return can_spell_with_options(options, set())

for word in words:
    if can_spell(word):
        print("YES")
    else:
        print("NO")