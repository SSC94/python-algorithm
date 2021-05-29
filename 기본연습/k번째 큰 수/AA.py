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

'''
n은 1~100사이의 자연수가 적힌 카드의 장수이고,
k로 위의 로직이 완료되어서 만들어진 리스트에서 k번째로 큰 수가 선택된다.
for문을 살펴보면 3가지 수를 모든 경우의 수로 뽑고 합을 해야하는데
m은 j+1부터 n까지 j는 i+1부터 n-1까지 i는 0부터(인덱스) n-2로
모든 경우의 수가 만들어진다.
'''