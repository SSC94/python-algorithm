import sys

sys.stdin = open("input.txt", "r")
n = int(input())
meeting = []

for i in range(n):
    s, e = map(int, input().split())
    meeting.append((s, e))

meeting.sort(key=lambda x:(x[1],x[0]))
end_time = 0
count = 0

for s, e in meeting:
    if s >= end_time:
        end_time = e
        count += 1

print(count)

# 추가 코드
# import sys
# sys.stdin = open('input.txt','r')
# n = int(sys.stdin.readline())
# tp_list = sorted([tuple(map(int,sys.stdin.readline().split())) for _ in range(n)],key = lambda x : (x[1],x[0]))
# count = end = 0
# for i in tp_list:
#     if end <= i[0]:
#         count += 1
#         end = i[1]
# print(count)


'''
한 개의 회의실이 있는데 이를 사용하고자 하는 n개의 회의들에 대하여 회의실 사용표를 만들
려고 한다. 각 회의에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하
면서 회의실을 사용할 수 있는 최대수의 알고리즘을 구하자. 단, 회의는 한번 시작하면 중간에 중
단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다.

해당 문제에서 우선 회의 시간을 끝나는 시간을 기준으로 오름차순으로 정렬한다.
그리고 첫 번째 회의가 끝나는 시간을 이 이후의 회의들의 시작 시간과 비교하여
끝나는 시간과 같거나 늦은 시간으로 시작하는 회의가 다음 회의가 된다.
하나의 리스트에 각 회의시간을 튜플로 묶어서 저장한다. 회의가 끝나는 시간으로
정렬할 때 .sort() 메서드나 sorted() 함수를 사용한다. 
key 매개변수는 하나의 인자를 받고, 정렬 목적을 위한 키를 리턴하는 함수가 되어야 한다.
여기서는 람다식을 사용하여 튜플들의 회의 시작과 끝나는 시간을 뒤집고, 오름차 순으로 정렬한다.
튜플에서 순서로 정렬할 때는 가장 앞부분을 기준으로 하기 때문이다.
'''
