"""
l1=[-10,0,10]
n=1
for i in range(0, len(l1)):
    for j in range(n, len(l1)):
        if l1[i] >= l1[j]:
            l1[i], l1[j] = l1[j],l1[i]
    if n<(len(l1)-1):
        n=n+1
print(l1[-2])
"""

n=int(input())
l=set(list(map(int,input().split())))
a=list(l)
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if (a[i] < a[j]):
            a[i],a[j]=a[j],a[i]

print(a[1])

"""                
l=[1,2,3,4,5,5,5,2,4]

a=len(a)
n=1
max=0
for i in range(0,a):
    for j in range(n,a):
        if(l[j] > l [i]):
            max=j
    l[i],l[max]=l[max],l[i]
    if n < a:
        n=n+1
print(l)
"""
