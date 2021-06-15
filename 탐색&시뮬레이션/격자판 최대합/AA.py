import sys

sys.stdin = open("input.txt","r")
n = int(input())
lis = [list(map(int,input().split())) for _ in range(n)]
sumMax = 0

for i in range(n):
    sum1 = sum2 = 0
    for j in range(n):
        sum1 += lis[i][j]
        sum2 += lis[j][i]
    if sum1 > sumMax :
        sumMax = sum1
    if sum2 > sumMax :
        sumMax = sum2

sum1 = sum2 = 0
for i in range(n):
    sum1 += lis[i][i]
    sum2 += lis[-1-i][-1-i]
if sum1 > sumMax :
    sumMax = sum1
if sum2 > sumMax :
    sumMax = sum2

print(sumMax)

# 추가 코드
# import sys
# sys.stdin = open('input.txt','r')
# n = int(sys.stdin.readline())
# lis = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
# max_num = sum_dia1 = sum_dia2 = 0
# for i in range(n):
#     sum_row = sum_col = 0
#     for j in range(n):
#         sum_row += lis[i][j]
#         sum_col += lis[j][i]
#     max_num = max(max_num,sum_row,sum_col)
# for i in range(n):
#     sum_dia1 += lis[i][i]
#     sum_dia2 += lis[-i-1][-i-1]
# max_num = max(max_num,sum_dia1,sum_dia2)
# print(max_num)


'''
자연수 N이 주어지면 N*N격자판이 만들어진다. 이 때 격자판 내부의 숫자들을
각 행의 합, 열의 합, 대각선의 합들을 비교하여 가장 큰 합을 구하는 알고리즘이다.

먼저 격자판의 요소들이 들어가는 리스트를 만든다. 해당 리스트를 만들 경우 리스트 컴프리헨션을 참고하자.
첫 번째 for문은 행과 열을 동시에 탐색하여 그 합을 비교하고 최고값을 sumMax에 저장한다.
두 번째 for문은 대각선 두개의 합을 구하는데 리스트 인덱싱을 활용한다.
'''
