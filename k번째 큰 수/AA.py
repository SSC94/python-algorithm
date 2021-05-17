import sys
sys.stdin=open("input.txt","rt")
n,k=map(int,input().split())
a=list(map(int,input().split()))
res=set()
for i in range(n-2):
    for j in range(i+1,n-1):
        for m in range(j+1,n):
            res.add(a[i]+a[j]+a[m])
res=list(res)
res.sort(reverse=True)
print(res[k-1])