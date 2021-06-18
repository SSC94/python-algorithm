import sys

sys.stdin = open("input.txt", "r")
n, m = map(int,input().split())
lis = list(map(int,input().split()))
lis.sort()
count = 0

while lis:
    if len(lis) == 1:
        lis.pop()
    else:
        p1, p2 = lis[0], lis[-1]
        if p1 + p2 <= m:
            lis.pop(0)
            lis.pop()
        else:
            lis.pop()
    count += 1
print (count)

# 추가 코드
# import sys
# sys.stdin = open('input.txt','r')
# n, m = map(int,sys.stdin.readline().split())
# lis = sorted(list(map(int,sys.stdin.readline().split())),reverse=True)
# lp = count = 0
# rp = n-1
# while lp <= rp:
#     if len(lis) == 1:
#         count += 1 
#         break
#     if lis[lp] + lis[rp] <= m:
#         lp += 1
#         rp -= 1
#     else:
#         lp += 1
#     count += 1
# print(count)


'''
타이타닉이 침몰하고 있다. 안에는 N명의 승객이 타고 있다.
구명보트를 타고 탈출해야 하는데 타이타닉에 있는 구명보트는
2명 이하로만 탈 수 있고, M kg 이하로 무게가 제한 되어 있다.
N명의 승객의 몸무게가 주어졌을 때, 승객 모두가 탈출하기 위한
구명보트의 최소 개수는 몇개인지 출력하는 알고리즘을 구하자.

승객의 몸무게가 주어진 리스트를 오름차 순으로 재배열하고,
가장 앞의 요소를 맨뒤에서 부터 차례로 찾아가면서 
몸무게가 M에 최대한 가까운 2명을 찾는다. 만약 못찾을 경우는
1명만 타는것으로 한다. 그 후에 1을 카운팅하고, 해당 승객들을 리스트에서 삭제한다.
반복문에서 해당 로직대로 찾지만 예외로 남은 승객이 몸무게와 상관없이
1명만 남을 경우도 생각해서 코드를 작성한다.
'''
