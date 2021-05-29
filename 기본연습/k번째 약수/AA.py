import sys
sys.stdin=open("input.txt","rt")
n,k=map(int,input().split())
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
    if count==k:
        print(i)
        break
else:
    print(-1)

'''
n,k에 input.txt에 있는 숫자 두개가 들어온다.
for문으로 변수i를 1부터 n까지 반복한다.
약수를 구하기 위한 로직으로 나누었을때 나머지가 0인 수를 찾는다.
그리고, k번째로 작은 수를 찾기 위한 로직으로
약수를 찾을 때 마다 count가 1씩 증가하여
결과적으로 k와 count가 같을때 i를 출력하고, 반복문을 멈춘다.
for~else로 for문이 정상종료가 되었을 경우 즉, 약수가 존재하지
않을 경우 -1을 출력한다.
'''