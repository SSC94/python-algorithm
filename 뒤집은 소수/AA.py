import sys
sys.stdin = open("input.txt","rt")
n=int(input())
lis=list(map(int,input().split()))

# def reverse(x):
#     tmp=[]
#     count=''
#     for i in x:
#         for j in range(len(str(i))):
#             if i%10==0:
#                 i=i//10
#                 continue
#             count+=str(i%10)
#             i = i // 10
#         tmp.append(int(count))
#         count=''
#     return(tmp)

def reverse(x):
    res=0
    while x>0:
        tmp=x%10
        x=x//10
        res=res*10+tmp
    return res

def isPrime(x):
    if x<2:
        return False
    for i in range(2,x):
        if x%i==0:
            return False
    else:
        return True

for i in lis:
    tmp = reverse(i)
    if isPrime(tmp):
        print(tmp,end=' ')

'''
N개의 자연수가 입력되면 각 자연수를 뒤집은 후 그 뒤집은 수가 소수이면 그 수를 출력하는 알고리즘이다.
예시로 397을 뒤집으면 793이 된다. 단, 240을 뒤집으면 첫 자리부터의 연속된 0은 무시하여 42가 된다.
뒤집는 함수인 reverse()와 소수인지 판별하는 함수 isPrime()을 작성해야 한다.

수를 뒤집을 때 %10 연산으로 가장 뒷자리의 숫자를 선택할 수 있다.
//10 연산으로 가장 뒷자리의 숫자를 제거 할 수 있다.
소수를 판별할 때 소수는 1과 자기자신만 나누어 지니 1과 자기자신을 제외하고,
다른 숫자에는 나누어 지지 않는 즉, 약수가 없어야 한다. 
숫자 범위도 range를 사용할 경우 2부터 자기자신 전까지를 범위로 한다.
'''