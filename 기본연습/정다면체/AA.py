import sys
sys.stdin=open("input.txt","rt")
n,m=map(int,input().split())
lis=[0]*(n+m+1)
idx=0
tmp=0
for x in range(1,n+1):
    for y in range(1,m+1):
        idx=x+y
        lis[idx]+=1
for i in lis:
    if i>tmp:
        tmp=i
for i in range(len(lis)):
    if lis[i]==tmp:
        print(i,end=' ')
        
# 추가 코드
# import sys
# sys.stdin = open('input.txt','r')
# n, m = map(int,sys.stdin.readline().split())
# dict1 = dict()
# max_num = 0
# for x in range(1,n+1):
#     for y in range(1,m+1):
#         dict1[x+y] = dict1.get(x+y,1) + 1
# max_num = max(dict1.values())
# for key,val in dict1.items():
#     if max_num == val:
#         print(key,end=' ')
        
'''
두 개의 정 n면체와 정 m면체의 두 개의 주사위를 굴려서 나올 수 있는
합 중 가장 확률이 높은 숫자를 구하고 확률이 같을 경우 오름차순으로 출력하는 알고리즘이다.
이중 for문 x,y는 주사위 눈이 1부터 시작하고, 각각 n과 m까지 숫자가 나오니
범위를 (1,n+1),(1,m+1)로 설정한다. 
빈리스트 lis[] 에는 인덱스가 두 눈의 합을 의미하고 매칭되는 값은 두 눈의 합이
나오는 경우의 수가 나올때마다 하나씩 카운팅 된다. 
두 번째 for문은 가장 확률이 높은 숫자를 구하는 로직이다.
세 번째 for문은 가장 확률이 높은 숫자들을 오름차 순으로 출력해낸다.
'''
