import sys

sys.stdin = open("input.txt","r")
n = input()
lis = [list(map(int,input().split())) for _ in range(n)]
sumApple = 0
startPoint = endPoint = n//2

for i in range(n):
    for j in range(startPoint, endPoint+1):
        sumApple += lis[i][j]
    if i<n//2:
        startPoint -= 1
        endPoint += 1
    else:
        startPoint += 1
        endPoint -= 1

print (sumApple)

# 추가 코드
# import sys
# sys.stdin = open('input.txt','r')
# n = int(sys.stdin.readline())
# lis = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
# lp, rp, count = n//2, n//2+1, 0
# for i in range(n):
#     count += sum(lis[i][lp:rp])
#     if i < n//2:
#         lp -= 1
#         rp += 1
#     else:
#         lp += 1
#         rp -= 1
# print(count)    

'''
사과나무 농장이 있는데 농장은 N*N 격자판(N의 크기는 항상 홀수이다.)으로 이루어져 있으며, 
각 격자안에는 한 그루의 사과나무가 심어져 있다. 사과를 수확할 때는 격자판이 다이아몬드 모양으로 수확하고,
나머지 격자의 사과들은 새들을 위해서 남겨놓는다. 이 때 수확한 모든 사과의 합을 구하는 알고리즘이다.
만약 5*5 격자이면 아래 그림처럼 수확한다.
x x o x x
x o o o x
o o o o o
x o o o x
x x o x x

투 포인터 알고리즘을 활용해서 각 행의 격자들을 검사하여 총합(sumApple)에 저장한다.
먼저 포인터가 가르키는 범위의 시작은 행의 중앙 격자 한개로 시작점(startPoint)과
끝지점(endPoint)를 n//2로 초기화하고, 행[i] for문 내부의 열[j] for문에서 사용되어
한행의 사과를 sumApple에 더하고, 행i가 중앙 이전 즉, 전체크기의 절반 이전에는
검사하는 열의 개수가 증가하므로 startPoint를 앞으로 당기는 -1을 하고, 
endPoint를 뒤로 보내는 +1을 하여 중앙 행 전까지 검사하는 열의 개수를 앞뒤로 한칸씩 늘린다.
그리고, 검사하는 행이 중앙부터는 다시 검사하는 열의 개수가 앞뒤로 한칸씩 줄어드니
startPoint를 +1을 하고, endPoint를 -1을 한 뒤 최종 sumApple을 출력한다. 
'''
