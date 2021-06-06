import sys

sys.stdin = open("input.txt", "r")
lis, m = map(int,input().split())
lis = list(map(int,str(lis)))
stack = []
for x in lis:
    while stack and m > 0 and stack[-1] < x:
        stack.pop()
        m -= 1
    stack.append(x)
if m:
    stack = stack[:-m]
res = ''.join(map(str,stack))
print (res)

'''
어떤 숫자들이 있다. 해당 숫자의 자리수들 중 m개의 숫자를 제거하여
가장 큰 수를 만들려고 한다. 만약 5276823이 주어지고 3개의 자릿수를
제거한다면 7823이 가장 큰 수가 된다.

스택 알고리즘을 사용한다. 가장 나중에 들어온 요소가 먼저 나가는 방식이다.
'''