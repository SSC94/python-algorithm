import sys

sys.stdin = open("input.txt", "r")
n = int(input())
lis = list(map(int,input().split()))
m = int(input())
lis.sort(reverse=True)
for _ in range(m):
    lis[0] -= 1
    lis[n-1] += 1
    lis.sort(reverse=True)
res = lis[0] - lis[n-1]
print (res)

'''
상자가 쌓여있는 줄이 N개인 창고가 있다. 
창고안에서 높이 조정을 M회 하는데 높이 조정은
가장 상자가 많이 쌓인 줄에서 하나를 빼서 
가장 상자가 적게 쌓인 줄에 하나를 쌓는 것이다.
만약 가장 많이 쌓이거나 적게 쌓인 줄이 여러곳이면
아무거나 선택해도 된다. M회의 높이 조정을 한 후 
가장 많이 쌓인 줄의 상자수와 가장 적게 쌓인 줄의 상자수의
차이를 출력하는 알고리즘을 구하자.

기본적인 리스트 조작 메서드들을 활용하여 출력하자.
'''