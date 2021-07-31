def solve(s):
    s = list(s)
    for i in range(len(s)):
        if i == 0:
            s[i] = s[i].upper()
        elif s[i] == ' ':
            s[i+1] = s[i + 1].upper()
    return ''.join(s)