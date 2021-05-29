import sys

sys.stdin = open("input.txt","r")
n=int(input())

# 방법 1
def sol(x):
    org=[]
    rev=[]
    tmp=[]
    for i in str(x):
        i=i.upper()
        org.append(i)
        tmp.append(i)
    for j in str(x):
        rev.append(tmp.pop())
    if org==rev:
        return 'YES'
    else:
        return  'NO'

for i in range(n):
    x=input()
    res=sol(x)
    print ('#{} {}'.format(i+1,res))

# 방법 2
# for i in range(n):
#     s=input()
#     s=s.upper()
#     for j in range(len(s)//2):
#         if s[j]!=s[-1-j]:
#             print("#%d NO"%(i+1))
#             break
#     else:
#         print("#%d YES"%(i+1))

# 방법 3
# for i in range(n):
#     s=input()
#     s=s.upper()
#     if s!=s[::-1]:
#         print("#%d NO"%(i+1))
#     else:
#         print("#%d YES"%(i+1))

'''
N개의 문자열 데이터를 입력받아 검사할 때 앞에서 읽거나 뒤에서 읽어도 같은 경우
즉, 회문 문자열이면 YES를 출력하고, 아니면 NO를 출력하는 알고리즘을 작성한다.
단, 대소문자는 구분하지 않는다.

3가지 방법으로 동일한 결과 출력
방법 1은 원본 배열과 뒤집은 배열을 만들어서 비교하는 함수를 만들었다.
방법 2는 문자열의 절반으로 반대쪽(-1-j)와 비교한다.
방법 3은 슬라이싱으로 간단하게 문자열을 뒤집어서 비교한다.
'''