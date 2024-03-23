a=list(map(int,input("enter numbers").split()))
b=[0]*len(a)


for i in range(len(a)-1):
        b[i]=a[i]+a[i+1]
b[i+1]=a[-1]
        
print(b)
