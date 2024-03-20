def solution(a):
    max_sum=-1
    d_set=[set(str(i)) for i in a]
    b_num=()
    for i in range(len(a)):
        for j in range (i+1,len(a)):
            if not d_set[i].intersection(d_set[j]):
                cur_sum=a[i]+a[j]
                if cur_sum > max_sum:
                    max_sum = cur_sum
                    b_num= (a[i],a[j])
    return max_sum

###
#a=[]
#n=int(input("length of array"))
#for i in range(0,n):
#    a[i]=int(input("enter the number")).split()
a=list(map(int,input("enter number").split()))
print(solution(a))
