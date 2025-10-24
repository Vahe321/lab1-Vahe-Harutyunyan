def naive_string_match(text, pattern):
    n = len(text)
    m = len(pattern)

    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break

        if match:
            print(f"Pattern found at index {i}")
text = "AABAACAADAABAABA"
pattern = "AABA"
naive_string_match(text, pattern)
