import sys

sys.stdin = open("input.txt","r")
n=input()
count=0
res=''

for i in n:
    if i.isdecimal()&(i!='0'):
        res+=i
else:
    res=int(res)

# 숫자를 뒤집고, 앞자리에 연속된 0을 제거하는 다른 방법(res=0 일 경우)
#   if i.isdecimal():
#       res=res*10+int(i)

for i in range(1,res+1):
    if res%i==0:
        count+=1
print(res,count,sep='\n')

'''
문자와 숫자가 섞여있는 문자열이 주어지면 그 중 숫자만 추출하여 그 순서대로 자연수를 만든다.
그리고 만들어진 자연수와 그 자연수의 약수 개수를 출력한다.
예시로 'tdksljt0st0s1sdc2qwr0sl'이라는 문자열이 주어지면 0,0,1,2,0을 추출하고,
이것을 자연수로 만들때는 가장 앞 자리 0은 무시하고, 출력하여 120을 출력한다.
그 다음줄에는 120의 약수의 개수를 출력한다.

첫 번째 for문에서 isdecimal()메서드와 0이 아닐때의 조건문을 사용하여 숫자인지 판별하고 
res변수에 숫자를 추출하여 순서대로 저장한다. isdigit()메서드는 자연수뿐만 아니라 숫자이기만 하면
True가 나오므로 여기서는 적합하지 않다.
두 번째 for문에서 약수의 개수를 구하여 
최종적으로 자연수가 저장된 res와 약수의 개수가 저장된 count를 한줄씩 출력한다.
'''