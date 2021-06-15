import sys

sys.stdin = open("input.txt","r")
n = int(input())
lis = [list(map(int,input().split())) for _ in range(n)]
lis.insert(0,[0]*(n+2)) # lis.insert(0,[0]*n)
lis.append([0]*(n+2)) # lis.append([0]*n)
count=0

for i in range(1,n+1): # for i in lis:
    lis[i].insert(0,0)      #     i.insert(0,0)
    lis[i].append(0)     #     i.append(0)

for i in range(1,n+1):
    for j in range(1,n+1):
        tmp=lis[i][j]
        up=lis[i-1][j]
        down=lis[i+1][j]
        left=lis[i][j-1]
        right=lis[i][j+1]
        if tmp>up and tmp>down and tmp>left and tmp>right:
            count+=1
print (count)

# 추가 코드
# import sys
# sys.stdin = open('input.txt','r')
# n = int(sys.stdin.readline())
# lis = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
# lis.insert(0,[0]*n)
# lis.append([0]*n)
# dx = [0,0,-1,1]
# dy = [-1,1,0,0]
# count = 0
# for i in lis:
#     i.insert(0,0)
#     i.append(0)
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if all(lis[i][j] > lis[i+dx[k]][j+dy[k]] for k in range(4)):
#             count += 1
# print(count)

'''
지도 정보가 N*N 격자판에 주어진다. 각 격자에는 그 지역의 높이가 쓰여져있다.
각 격자판의 숫자 중 자신의 상하좌우 숫자보다 큰 숫자는 봉우리 지역이다.
그리고 격자의 가장자리는 0으로 초기화 되었다고 가정한다.
봉우리 지역이 몇 개 있는지 알아내는 알고리즘을 구하자. 
예시로 N=3이고, 격자판의 숫자가 다음 과 같다면 봉우리는 7,6,5로 3개이다.
ex)
0 0 0 0 0
0 7 2 6 0
0 1 5 3 0
0 2 3 1 0
0 0 0 0 0

N*N개의 격자판을 lis에 생성하고, 가장자리는 우선 첫 행과 끝 행에 요소가 전부 0인
리스트를 추가하고, 첫 번째 for문으로 기존의 0이 아닌 숫자가 있는 각 행의 처음과 끝
열에 0을 추가한다. 다음으로 봉우리를 구해야 하므로 0이 아닌 격자들을 모두 검사하는
두 번째 for문을 만들어서 각 격자 요소들의 상하좌우 변수(up,down,left,right)를 만들고,
내부의 if문으로 격자의 요소가 상하좌우 변수와 비교하여 가장 크면 전체 봉우리 개수를
구하는 변수 count에 +1을 하고, 최종적으로 count를 출력한다.

※ 주석처리한 코드로 더 간단하게 구현가능하다.
첫 번째 for문은 얕은 복사(shallow copy)를 활용하여 
lis의 각 행의 시작과 끝에 0을 할당 할 수 있고, 
상하좌우를 비교하는 for문에서는
all()함수와 제너레이터 표현식을 잘 익히면 더 효율적인 코드를 작성할 수 있다.
'''

