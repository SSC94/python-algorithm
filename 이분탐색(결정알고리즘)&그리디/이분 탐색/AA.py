import sys

sys.stdin = open("input.txt","r")
n,m = map(int,input().split())
lis = list(map(int,input().split()))
lis.sort()
lp = 0
rp = n-1

while lp <= rp :
    mid = (lp+rp) // 2
    if lis[mid] == m :
        print (mid + 1)
        break
    elif lis[mid] < m :
        lp = mid + 1
    else :
        rp = mid - 1

'''
임의의 N개의 숫자가 입력으로 주어진다. N개의 수를 오름차순으로 정렬한 다음 N개의 수 
중 한 개의 수인 M이 주어지면 이분검색으로 M이 정렬된 상태에서 몇 번째에 있는지 구하는 
알고리즘을 작성하자. 단, 중복은 존재 하지 않는다.
예시로 N이 3이고, M은 5 N개의 숫자는 7 1 5 의 경우 오름차순으로 1 5 7로 정렬하고,
5의 위치인 2를 출력한다.

해당 문제는 파이썬의 리스트 메서드중 index()를 이용하면 간편하지만 이분 탐색 알고리즘이므로
탐색 범위를 두 부분으로 분할해서 값을 찾는 코드를 구현하자.
왼쪽 포인터인 lp, 오른쪽 포인터인 rp를 할당하고, while문으로 lp와 rp가 곂쳐질 때 까지 탐색을 한다.
mid는 lp와 rp의 중간 위치를 표현하고, lis에서 mid위치가 m과 같다면 그대로 위치값을 출력하고,
while문을 종료시킨다. 만약 같지 않고, m보다 작다면 최소한 현 mid의 순서보다 뒤에 있으므로 
lp를 mid+1로 옮기고, m보다 크다면 현 mid의 순서보다 앞에 있다는 의미이므로 rp를 mid-1로 옮긴다.
'''