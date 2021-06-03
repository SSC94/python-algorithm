import sys

sys.stdin = open("input.txt", "r")


def Count(capacity):
    record = 1
    sum = 0
    for i in lis:
        if sum + i > capacity:
            record += 1
            sum = i
        else:
            sum += i
    return record


_, m = map(int, input().split())
lis = list(map(int, input().split()))
lp, rp = 1, sum(lis)
lisMax = max(lis)
res = 0

while lp <= rp:
    mid = (lp + rp) // 2
    if mid >= lisMax and Count(mid) <= m:
        res = mid
        rp = mid - 1
    else:
        lp = mid + 1

print(res)

'''
한 가수의 여러 뮤직비디오를 DVD에 담으려고 한다.  DVD를
녹화할 때에는 음악의 순서들이 바뀌면 안된다. 즉, 1번 노래와
5번 노래를 같은 DVD에 녹화하기 위해서는 1번과 5번 사이의 
모든 노래도 같은 DVD에 녹화해야 한다. 또한 하나의 노래를
쪼개서 두 개 이상의 DVD에 녹화하면 안된다.
그리고 모든 노래를 M개의 DVD에 배분하여 녹화하려고 한다.
배분하는 기준은 입력되는 노래의 재생 길이(분)을 숫자로 표현하여
DVD의 용량에 넘어가지 않는 선에서 최대로 나누어 담는다.
이 때 사용되는 DVD의 용량을 최소 크기로 하려고 한다.
이 DVD의 최소 용량 크기를 출력하는 알고리즘을 구하자.

Count함수는 녹화하는 DVD의 개수를 입력받는 인자(capacity)의 기준으로 나누어주는 함수이다.
마찬가지로 이분탐색 알고리즘을 사용하여 나누는 용량을 최소값 1부터 최대값 모든 용량의 합까지로
구한다. 단 하나 더 추가 조건은 중간에 Count함수를 사용하여 나누어 녹화하는 DVD개수가 m보다 커지면
안되는 것을 추가로 검사한다.
'''