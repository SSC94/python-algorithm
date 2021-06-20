import sys

sys.stdin = open("input.txt","r")
lis=list(range(21))

for _ in range(10):
    a,b=map(int,input().split())
    for i in range((b-a+1)//2):
        lis[a+i],lis[b-i]=lis[b-i],lis[a+i]

del lis[0]

for i in lis:
    print(i,end=' ')
    
# 추가 코드
# import sys
# sys.stdin = open('input.txt','r')
# lis = [x for x in range(21)]
# def sol(a,b):
#     lis[a:b+1] = lis[b:a-1:-1]
# for _ in range(10):
#     a, b =map(int,sys.stdin.readline().split())
#     sol(a,b)
# lis.remove(0)
# print(lis)

'''
1부터 20까지 숫자가 하나씩 쓰인 20장의 카드가 오름차순으로 있다.
각 카드의 위치는 1부터 20까지로 나타낸다. 이 카드들은 다음과 같은 규칙으로 위치를 바꾼다.
구간[a,b](단,1<=a<=b<=20)이 주어지면 위치 a부터 b까지의 카드를 역순으로 재배치 한다.
예시로 처음에 구간이[5,10]으로 주어지면, 위치 5부터 10까지의 카드를 5,6,7,8,9,10이 아닌
10,9,8,7,6,5로 놓는다. 이러한 과정을 10개의 구간이 주어지고, 주어진 구간을 규칙대로 
순서를 뒤집는 작업을 연속해서 처리한 뒤 최종 카드들의 배치를 출력하는 알고리즘을 구하자.

1부터 20까지의 위치를 나타내기 위해 리스트(lis)를 생성 다만 0이 포함된 이유는
인덱스 순서와 위치 순서를 혼동하지 않기 위해 0을 포함하여 21개 요소를 가진 리스트를 만든다.
2중 for문에서 (b-a+1)//2 의 부분은 카드를 주어진 구간으로 역배치 할 경우 처음부터 끝까지
검사하는 것이 아닌 절반만 검사하면 되므로 해당 로직을 사용함
a,b=b,a로 간단하게 값을 뒤 바꿀 수 있다.
끝으로 인덱스0의 요소를 삭제하고, 리스트 내부의 요소들을 출력한다.
'''
