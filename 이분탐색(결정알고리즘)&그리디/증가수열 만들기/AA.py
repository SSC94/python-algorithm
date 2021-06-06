import sys

sys.stdin = open("input.txt", "r")
n = int(input())
# lis = list(map(int,input().split()))
# res,count = 0, 0
# res_str = ''
# while True:
#     if len(lis) == 1:
#         if count < lis[0]:
#             res += 1
#             res_str += 'L'
#             print(res, res_str, sep='\n')
#             break
#         else:
#             print(res, res_str, sep='\n')
#             break
#     if lis[0] < lis[-1]:
#         if count < lis[0]:
#             res += 1
#             res_str += 'L'
#             count = lis[0]
#             lis.pop(0)
#         elif count < lis[-1]:
#             res += 1
#             res_str += 'R'
#             count = lis[-1]
#             lis.pop()
#         else:
#             print(res, res_str, sep='\n')
#             break
#     else:
#         if count < lis[-1]:
#             res += 1
#             res_str += 'R'
#             count = lis[-1]
#             lis.pop()
#         elif count < lis[0]:
#             res += 1
#             res_str += 'L'
#             count = lis[0]
#             lis.pop(0)
#         else:
#             print(res, res_str, sep='\n')
#             break


a=list(map(int, input().split()))
lt=0
rt=n-1
last=0
res=""
tmp=[]
while lt<=rt:
    if a[lt]>last:
        tmp.append((a[lt], 'L'))
    if a[rt]>last:
        tmp.append((a[rt], 'R'))
    tmp.sort()
    if len(tmp)==0:
        break;
    else:
        res=res+tmp[0][1]
        last=tmp[0][0]
        if tmp[0][1]=='L':
            lt=lt+1
        else:
            rt=rt-1
    tmp.clear()

print(len(res))
print(res)

'''
1부터 N까지의 모든 자연수로 구성된 길이 N의 수열이 주어진다. 
이 수열의 왼쪽 맨 끝 숫자 또는 오른쪽 맨 끝 숫자 중 하나를 가져와 나열하여 가장 긴 증가수열
을 만든다. 이 때 수열에서 가져온 숫자(왼쪽 맨 끝 또는 오른쪽 맨 끝)는 그 수열에서 제거된다. 
예를 들어 2 4 5 1 3 이 주어지면 만들 수 있는 가장 긴 증가수열의 길이는 4이다.
맨 처음 왼쪽 끝에서 2를 가져오고, 그 다음 오른쪽 끝에서 3을 가져오고, 왼쪽 끝에서 4, 
왼쪽 끝에서 5를 가져와 2 3 4 5 증가수열을 만들 수 있다. 출력은 첫째 줄에 최대 증가수열의 길이이고,
두 번째 줄에는 가져간 순서대로 왼쪽 끝에서 가져갔으면 'L', 오른쪽 끝에서 가져갔으면 'R'을 입력한
문자열을 출력한다. 단 마지막에 남은 값은 왼쪽 끝으로 생각한다.


'''