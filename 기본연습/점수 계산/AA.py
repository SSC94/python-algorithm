import sys
sys.stdin = open("input.txt","r")
n=int(input())
lis=list(map(int,input().split()))
total=0
tmp=0
for i in range(n):
    if lis[i]:
        tmp+=1
        total+=tmp
    else:
        tmp=0

print (total)

'''
OX 문제의 채점 점수를 구하는 알고리즘이다. 입력되는 첫번째 변수는 문제의 개수이고,
두번째 변수에는 OX문제를 맞춘 결과가 저장된 배열이다. 배열에는 맞출경우 1이 입력되있고,
오답일 경우 0으로 입력되어 있다. 채점시에는 맞춘 개수만큼 +1을 하는데 만약 연속으로 맞춘 문제들의 경우
가산점이 1점씩 늘어난다. 예시로 3문제를 연속으로 맞추었을 경우 1+2+3 총 6점이 되고, 문제를 틀린 뒤
다시 문제를 맞추면 다시 1점으로 채점한다.

두개의 변수 총합점수(total)과 연속점수(tmp)를 0으로 초기화 한 뒤
for문으로 문제 수 만큼 반복해 채점한다. 만약 맞추었으면 tmp에 1점을 추가하고,
total에는 tmp를 더하여 연속되는 점수를 계산한다. 만약 틀렸을 경우 tmp를 다시 0으로
초기화한다.
'''