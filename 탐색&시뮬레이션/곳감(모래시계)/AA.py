import sys

sys.stdin = open("input.txt","r")
n = int(input())
lis = [list(map(int,input().split())) for _ in range(n)]
m = int(input())

for _ in range(m):
    row,direction,rotation = map(int,input().split())
    tmp=0
    if direction:
        for _ in range(rotation):
            tmp = lis[row-1].pop()
            lis[row-1].insert(0,tmp)
    else:
        for _ in range(rotation):
            tmp = lis[row-1].pop(0)
            lis[row-1].append(tmp)

startPoint = 0
endPoint = n
res = 0

for i in range(n):
    for j in range(startPoint,endPoint):
        res += lis[i][j]
    if i < n//2:
        startPoint += 1
        endPoint -= 1
    else:
        startPoint -= 1
        endPoint += 1

print(res)

# 추가 코드
# import sys
# sys.stdin = open('input.txt','r')
# n = int(sys.stdin.readline())
# lis = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
# m = int(sys.stdin.readline())
# lp = count = 0
# rp = n
# for i in range(m):
#     row, direction, num = map(int,sys.stdin.readline().split())
#     if direction:
#         for _ in range(num):
#             lis[row-1].insert(0,lis[row-1].pop())
#     else:
#         for _ in range(num):
#             lis[row-1].append(lis[row-1].pop(0))
# for i in range(n):
#     count += sum(lis[i][lp:rp])
#     if i < n//2:
#         lp += 1
#         rp -= 1
#     else:
#         lp -= 1
#         rp += 1
# print(count)

'''
곳감을 만들기 위한 N*N 격자판이 있다. 격자판 각 한개안의 숫자는 말리고 있는 감의 수 이다.
그런데 특정위치의 감은 잘 마르지 않아 격자의 행을 기준으로 왼쪽, 또는 오른쪽으로 회전시켜 
위치를 변경해서 감을 말린다. 만약 회전명령이 2 0 3이면 2번째 행을 왼쪽으로 3만큼 이동시킨다.
ex) 12 39 30 23 11 -> 23 11 12 39 30 , 이처럼 회전명령 첫 번째 수는 행번호, 두 번째 수는
방향인데 0은 왼쪽, 1은 오른쪽이다. 세 번째 수는 회전하여 이동하는 격자의 수다. M개의 회전명령을 실행하고
아래의 모양과 같은 모래시계 모양의 영역에는 감 이 총 몇개가 있는지 알고리즘을 구하자.
o o o o o
x o o o x
x x o x x
x o o o x
o o o o o

먼저 각 변수 및 리스트를 만든다.
n : N*N 격자판의 크기
lis : 격자판 내부에 들어갈 요소(곳감 개수)
m : 회전명령의 횟수
row : 회전명령을 실행하는 행 번호(인덱싱할 경우 -1을 해준다.)
direction : 회전명령을 실행하는 방향(왼쪽 - 0, 오른쪽 - 1)
rotation : 회전명령으로 움직이는 횟수

첫 번째 for문에는 리스트의 요소 추가 제거 함수들을 사용하여
오른쪽으로 움직이는 경우 행의 맨뒤의 요소를 lis에서 제거하여 tmp에 추가하고,
다시 tmp를 lis의 가장 앞부분에 붙인다.
반대로 왼쪽으로 움직이는 경우 행의 가장 앞부분의 요소를 lis에서 제거하여
tmp에 추가하고, 다시 tmp를 lis의 가장 뒷부분에 붙인다.

다음으로 모래시계 모양으로 격자의 요소합을 구하는 방법은
투 포인터를 이용하여 처음에는 시작점(startPoint)를 0으로 설정하고,
끝점(endPoint)를 n으로 설정하여, 첫 행의 모든 요소를 가리키게 된다.
두 번째 for문으로 각 행들을 검사하여 포인터들의 범위 안의 요소들을 res에 전부 더하고,
if문으로 행의 번호(i)가 전체 배열의 크기의 절반 이전에는 startPoint를 +1하고, 
endPoint를 -1하여 포인터 범위를 줄이고, 행의 번호가 절반이후에는 
startPoint를 -1하고, endPoint를 +1하여 포인터 범위를 늘린다.
모든 과정을 마치고 최종 합을 출력한다.
'''

