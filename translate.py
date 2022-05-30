translation_table = {
    "j": "k",
    "m": "n",
    "a": "u"
}
line = "James John"
translated_line = line.lower().translate(str.maketrans(translation_table))

result = []

for i in range(len(line)):
    line_char = line[i]
    tranlated_char = translated_line[i]
    if line_char.upper() != line_char:
        result.append(tranlated_char)
    else:
        result.append(tranlated_char.upper())

result = "".join(result)

print(result)