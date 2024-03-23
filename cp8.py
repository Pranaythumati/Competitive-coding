if __name__ == '__main__':
    n = int(input("e"))
    a = list(map(int, input().split()))
    m=1
    l=len(a)
    for i in range (0,l):
        for j in range(m,l):
            if (a[i] < a[j]):
                a[i],a[j] = a[j],a[i]
                m=m+1
    s=set(a)
    a=list(s)
    print(a)
            
