import sys

sys.stdin = open("input.txt", "r")
n, m = map(int, input().split())
lis = []
for _ in range(n) :
    lis.append(int(input()))
lp, rp = 1, max(lis)
count = 0

while lp <= rp :
    mid = (lp + rp) // 2
    count = sum(x // mid for x in lis)

    if count >= m :
        res = mid
        lp = mid + 1
    else :
        rp = mid - 1

print (res)

'''
학원에서 각각 길이가 다른 K개의 랜선을 가지고 있다.
이 랜선들을 모두 N개의 같은 길이의 랜선으로 자르고 싶다.
예시로 300cm짜리 랜선에서 140cm 짜리 랜선을 두 개 잘라내면
20cm는 버려야 한다. 다만 자를 때 손실되는 길이는 없다고 가정하고,
기존의 K개의 랜선으로 N개의 랜선을 만들 수 없는 경우는 없다고 가정하자.
그리고 항상 cm단위이다. 이 때 만들수 있는 랜선의 최대 길이는 
몇인지 구하는 알고리즘이다.

길이가 다른 K개의 랜선 길이 숫자가 입력 받을 때 한 줄씩 띄어져 있으므로 for문으로
하나씩 lis에 추가한다. 그리고 자르는 길이의 시작범위(lp)와 끝나는 범위(rp)를 각각
1과 lis의 최대값으로 할당한다. 반복문은 lp가 rp보다 커지기 전까지 반복한다.
lp와 rp의 중간값인 mid는 K개의 랜선을 자르는 기준 크기가 된다.
mid로 모든 랜선을 자르면 그 자른 횟수를 모두 더해서 count에 할당한다.
그 후에 자른 횟수인 count가 만들어야 하는 개수인 N과 같거나 큰 지 if문으로 검사한다.
만약 크거나 같다면 그 때 mid값이 구해야 하는 최대 길이인 res로 할당되고, 
mid의 최대 길이를 구해야 하니 자르는 횟수를 가능하면 N에 맞추는게 좋으므로
범위 최소값 lp를 mid+1로 한다.
그렇지 않다면 범위 최대값 rp를 mid-1을 하고, 반복문 종료 후 res를 출력한다.
'''