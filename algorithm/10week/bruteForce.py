def bruteForce(p,t,k):
    M = len(p)
    N = len(t)
    i = k
    j = 0

    while j<M and i<N:
        if t[i] != p[j]:
            i -= j
            j = -1
        i += 1
        j += 1
    if j == M: return i-M
    else: return i

text = 'ababacabcbababcacacbcaababca'
pattern = 'ababca'
M = len(pattern)
N = len(text)
K = 0

while True:
    pos = bruteForce(pattern,text,K)
    K = pos + M
    if K < N: print('패턴이 나타난 위치: ',pos)
    else:
        text = text + '\0'
        break
print('string 탐색 종료')