def subseq(i, s, k):
    if i == len(s):
        k.append(''.join(k.copy()))
        return
    k.append(s[i])
    subseq(i + 1, s, k)
    k.pop()
    subseq(i + 1, s, k)
    return k
s = input()
print(subseq(0, s, []))

