def boyer(P, T):
    m = len(P)
    n = len(T)
    if m > n: return -1
    skip = []
    for k in range(256): skip.append(m)
    for k in range(m - 1): skip[ord(P[k])] = m - k - 1
    skip = tuple(skip)
    k = m - 1
    while k < n:
        j = m - 1; i = k
        while j >= 0 and T[i] == P[j]:
            j -= 1; i -= 1
        if j == -1: return i + 1
        k += skip[ord(T[k])]
    return -1

if __name__ == '__main__':
    T = "a aula esta padrao hoje"
    P = "padrao"
    s = boyer(P, T)
    if s > -1:
        print ('padrão encontrado na(s) linhas(s) posicão(ões)',s)
