import sys
sys.stdin=open("input.txt","rt")
n=int(input())
a=list(map(int,input().split()))
tmp=0

# def digit_sum(x):
#     sum=0
#     while x>0:
#         sum+=x%10
#         x=x//10
#     return sum

def digit_sum(x):
    sum=0
    for i in str(x):
        sum+=int(i)
    return sum

for i in a:
    sum=digit_sum(i)
    if tmp<sum:
        tmp=digit_sum(i)
        res=i
print(res)


'''
자릿수의 합이 가장 큰 자연수를 구하는 알고리즘이다.
만약 자릿수의 합이 같을 경우는 입력순으로 먼저인 숫자를 출력한다.

먼저 자릿수의 합을 구하는 함수 digit_sum(x)을 생성한다.
for문으로 리스트a의 각 요소들의 합을 비교하여 
합이 가장 큰 요소를 출력한다.
'''