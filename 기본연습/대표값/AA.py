import sys
sys.stdin = open("input.txt","rt")
n=int(input())
a=list(map(int,input().split()))
avg=round(sum(a)/n)
minVal=100
for idx, x in enumerate(a):
    tmp=abs(x-avg)
    if tmp<minVal:
        minVal=tmp
        score=x
        res=idx+1
    elif tmp==minVal:
        if x>score:
            score=x
            res=idx+1
print(avg,res)

# 추가 코드
# import sys
# sys.stdin = open('input.txt','r')
# n = int(sys.stdin.readline())
# lis = list(map(int,sys.stdin.readline().split()))
# dict1 = dict()
# res = []
# for i in range(1,n+1):
#     dict1[i] = lis[i-1]
# avg = round(sum(dict1.values())/n)
# for key, val in dict1.items():
#     if avg == val:
#         res.append(key)
# res = max(res)
# print(avg,res)

'''
round()소수 첫째자리 반올림 함수이다.
enumerate()는 순서가 있는 자료형(list, set, tuple, dictionary, string)의 인덱스와 값을 반환해준다.
minVal에는 평균과의 차이의 절대값중 가장 작은값이 입력된다.
score에는 현재 평균과 가장 차이가 안나는 점수가 입력된다.
res에는 현재 평균과 가장 차이가 안나는 점수의 학생번호가 인덱스로 입력된다. 인덱스는 0부터 시작하니 +1을 해준다.
정리하면 점수의 평균값과 평균값에 가장 근접하면서 가장 높은 점수의 학생번호를 출력해준다. 
'''
