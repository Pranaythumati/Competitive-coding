sub={}
n=int(input("enter number of subjects:"))
for i in range(0,n):
    sub[input('enter the name of the sub:')[i]]=int(input("enter marks:"))
print(sub)

for i in sub.items():
    totalmarks=0
    totalmarks=totalmarks+sub.item[i]
avg=totalmarks/n
print(avg)
