def bad_char_table(pattern):
    table = {}
    for i in range(len(pattern)):
        table[pattern[i]] = i
    return table


def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)
    bad_char = bad_char_table(pattern)

    s = 0
    while s <= n - m:
        j = m - 1


        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1

        if j < 0:
            print(f"Pattern found at index {s}")

            s += (m - bad_char.get(text[s + m], -1)) if s + m < n else 1
        else:
            s += max(1, j - bad_char.get(text[s + j], -1))
text = "HERE IS A SIMPLE EXAMPLE"
pattern = "EXAMPLE"
boyer_moore(text, pattern)
