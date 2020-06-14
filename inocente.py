

i=0
j=0
k=0
m=0
n=0




def ehSufixo(P, m, T, k):

    if (k >= m and m >= 0):
        l = m

        while (l >= 1 and P[l - 1] == T[k - m + l - 1]):
            l=l-1;

        if (l >= 1):
            return 0;

        else:
            return 1

    else:
        return




def inocente(P, m, T,n):
    flag=0
    print("\nIndices: ")
    for k in range(m,n):
        if (ehSufixo(P, m, T, k) == 1):
            if (flag == 0):
                print(k)
                flag=1
            else:
                print(k)

    print("")

P=[]
T=[]
vetor_t='000010001010001'
vetor_p='0001'
for i in vetor_p:
    P.append(i)
for j in vetor_t:
    T.append(j)

n = len(T)
m = len(P)

inocente(P,m,T,n)
