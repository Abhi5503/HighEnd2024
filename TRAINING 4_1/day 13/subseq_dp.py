
s1 = "AGGTAB"
s2 = "GXTXAYB"
m = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

#dp table..

for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
        if s1[i - 1] == s2[j - 1]:
            m[i][j] = m[i - 1][j - 1] + 1
        else:
            m[i][j] = max(m[i - 1][j], m[i][j - 1])

print(m[len(s1)][len(s2)])

