import sys

sys.stdin = open("input.txt","r")
lis = [list(map(int,input().split())) for _ in range(7)]
count = 0

for i in range(3) :
    for j in range(7) :
        tmp = lis[j][i:i+5]
        if tmp == tmp[::-1] :
            count += 1
        for k in range(2):
            if lis[i+k][j] != lis[i+4-k][j] :
                break
        else :
            count += 1

print (count)

# 추가 코드
# import sys
# sys.stdin = open('input.txt','r')
# lis = [list(map(int,sys.stdin.readline().split())) for _ in range(7)]
# count = 0
# for i in range(3):
#     for j in range(7):
#         tmp = lis[j][i:i+5]
#         if tmp == tmp[::-1]: count += 1
#         if lis[i][j] == lis[i+4][j] and lis[i+1][j] == lis[i+3][j]: count += 1
# print(count)

'''
1부터 9까지의 자연수로 채워진 7*7 격자판이 주어지면 격자판 위에서 
가로방향 또는 세로방향으로 길이 5자리(5칸) 회문수가 몇 개 있는지 알고리즘을 구하자.
회문수란 121 같이 앞이나 뒤에서 읽어도 같은 수를 말한다.
'''



