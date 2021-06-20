import sys
sys.stdin = open("input.txt","rt")
n=int(input())
ch=[0]*(n+1)
count=0
for i in range(2,n+1):
    if ch[i]==0:
        count+=1
        for j in range(i,n+1,i):
            ch[j]=1
print (count)

# 추가 코드
# import sys
# sys.stdin = open('input.txt','r')
# n = int(sys.stdin.readline())
# count = 1
# for i in range(3,n+1):
#     for j in range(2,i):
#         if i % j == 0:
#             break
#     else:
#         count += 1
# print(count)

'''
자연수 N이 입력되면 1부터 N까지의 소수의 개수를 출력하는 알고리즘이다.
리스트 ch는 각 인덱스가 0부터 N까지의 수 범위이다.
count는 소수의 개수를 카운팅한다.
소수는 1과 자기자신으로밖에 나누어 떨어지지 않는 1이외의 정수이다.
첫 번째 for문의 로직은 2부터 N까지의 숫자범위를 반복해서 실행한다.
ch[i]는 숫자2부터 검사를 하여 값이 0이므로 카운팅을 한다.
그 후에 내부의 for문으로 카운팅한 숫자의 배수의 값을 1로 만든다.
즉, for문이 동작하면 숫자2 카운팅 -> 숫자 2의 배수는 1로 처리 -> 숫자3 카운팅 -> 숫자 3의 배수는 1로처리
-> 숫자 4는 값이 1이므로 카운팅하지 않고 다음 숫자진행 -> 숫자5 카운팅 ->......
이 과정들을 숫자 N까지 반복한 뒤 count를 출력한다.
'''
