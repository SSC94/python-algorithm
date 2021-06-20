import sys

sys.stdin = open("input.txt","r")
a=int(input())
lis1=list(map(int,input().split()))
b=int(input())
lis2=list(map(int,input().split()))
p1=p2=0
res=[]

while p1<a and p2<b:
    if lis1[p1]<=lis2[p2]:
        res.append(lis1[p1])
        p1+=1
    else:
        res.append(lis2[p2])
        p2+=1

if p1<a:
    res=res+lis1[p1:]
else:
    res=res+lis2[p2:]

for i in res:
    print(i,end=' ')
    
# 추가 코드
# import sys
# sys.stdin = open('input.txt','r')
# a = int(sys.stdin.readline())
# list_a = list(map(int,sys.stdin.readline().split()))
# b = int(sys.stdin.readline())
# list_b = list(map(int,sys.stdin.readline().split()))
# res = []
# for i in list_a: res.append(i)
# for i in list_b: res.append(i)
# print(sorted(res))
    
'''
오름차순으로 정렬이 된 두 리스트가 주어지면 두 리스트를 오름차순으로 합쳐 출력하는 알고리즘이다.
예시로 첫 번째 리스트의 크기가 3이고, 그 리스트의 원소가 1 3 5로 주어졌다.
두 번째 리스트의 크기가 5이고, 그 리스트의 원소가 2 3 6 7 9로 주어졌을 때,
출력은 1 2 3 3 5 6 7 9 이다.

두 리스트의 포인터가 움직인다는 개념을 사용한다. lis1의 요소와 lis2의 요소를 가장 앞부분부터
하나씩 비교하여 작은쪽(같을 경우 lis1)의 요소를 빈 리스트(res)에 추가하고, 추가시킨 리스트의
포인터를 한칸씩 앞으로 움직인다. 이 과정을 반복하여 어느 한 포인터가 리스트의 크기만큼의 숫자가
되었을 때, while문을 종료시키고, if문으로 남은 한 리스트의 남은 부분을 res에 붙이고, 출력한다.
'''
