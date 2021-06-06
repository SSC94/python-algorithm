import sys

sys.stdin = open("input.txt", "r")
n = int(input())
lis = [list(map(int,input().split())) for _ in range(n)]
lis.sort(reverse=True)
count = 0
tmp = 0
# for i in lis:
#     if i[1] > tmp:
#         count += 1
#         tmp = i[1]
for x, y in lis:
    if y > tmp:
        count += 1
        tmp = y
print(count)



'''
씨름 선수를 뽑기 위해 공고를 냈다. N명의 지원자가 지원했고,
선발기준은 만약 A라는 지원자보다 키도 크고 몸무게도 무거운 지원자가
존재한다면 A지원자는 탈락한다. 해당 조건으로 지원자를 뽑을 경우
몇명이 뽑히는지 알고리즘을 구하자.

먼저 몸무게나 키 둘중 하나를 기준으로 내림차순으로 지원자의
정보를 정렬하여 리스트에 저장한다. 그리고 뽑히는 기준인
최소 한개 이상의 조건은 무조건 다른 지원자들 보다 숫자가
커야하니 기준이 아닌 다른 한 조건을 반복문으로 하나씩 검사하며
이전보다 최대값이 나올경우 지원자 숫자 count를 하나씩 더한다.
'''