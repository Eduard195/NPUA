string = "sdgadfjigsd"


def bad_char_table(pattern):
    table = [-1] * 256
    for i, ch in enumerate(pattern):
        table[ord(ch)] = i
    return table


def boyer_moore(text, pattern):
    bad_char = bad_char_table(pattern)
    m, n = len(pattern), len(text)
    s = 0

    while s <= n - m:
        j = m - 1

        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1

        if j < 0:
            return s
        else:
            s += max(1, j - bad_char[ord(text[s + j])])

    return "No such pattrn"

print(boyer_moore(string, "dfj"))
