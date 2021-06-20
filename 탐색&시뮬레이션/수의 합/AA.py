import sys

sys.stdin = open("input.txt","r")
n,m=map(int,input().split())
lis=list(map(int,input().split()))
lp=0
rp=1
total=lis[0]
count=0
while True:
    if total<m:
        if rp<n:
            total+=lis[rp]
            rp+=1
        else:
            break
    elif total==m:
        count+=1
        total-=lis[lp]
        lp+=1
    else:
        total-=lis[lp]
        lp+=1

print(count)

# 추가 코드
# import sys
# sys.stdin = open('input.txt','r')
# n, m = map(int,sys.stdin.readline().split())
# lis = list(map(int,sys.stdin.readline().split()))
# lp, rp, count = 0, 1, 0
# while lp < rp+1 and rp < n+1:
#     if sum(lis[lp:rp]) == m:
#         count += 1
#         lp += 1
#     elif sum(lis[lp:rp]) < m: rp += 1
#     else: lp += 1
# print(count)

'''
N개의 수로 된 수열 A[1],A[2], ..., A[N] 이 있다. 이 수열의 i번째 수부터
j번째 수까지의 합 A[i]+A[i+1]+...A[j-1]+A[j]가 M이 되는 경우의 수를 구하는 알고리즘
예시로 N이 8이고 M이 3이며 1 2 1 3 1 1 1 2 인 수열이 있을 경우 M이 3이되는 경우의 수는
5가지이다. 

투 포인터 알고리즘을 사용하여 부분합(total)이 목표값(m)보다 작을 경우 total에 
오른쪽포인터(rp)값을 더하고, rp를 한칸 앞으로 이동시킨다.
total이 m과 같을 경우 경우의 수(count)를 1증가시키고, total에 왼쪽포인터(lp)값을 뺀 뒤,
lp를 한칸 앞으로 이동시킨다. 그리고, total이 m보다 클 경우 total에 lp값을 뺀 뒤,
lp를 한칸 앞으로 이동시킨다. 여기서 total이 m보다 작을 경우에서 rp를 한칸 앞으로 이동시킬때
rp가 수열의 크기(n)과 같아지면 더 이상 부분합이 없으므로 반복문을 종료시킨다. 
'''
