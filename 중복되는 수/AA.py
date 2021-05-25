arr=[1,2,3,3,3,3,4,4]
# arr=[3,2,4,4,2,5,2,5,5]
# arr=[3,5,7,9,1]

def solution(arr):
    arr.sort()
    res=[0]*(arr[-1]+1)
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i]==j:
                res[j]+=1
    res=[x for x in res if x!=0 and x!=1]
    if res==[]:
        print(-1)
    else:
        print(res)
solution(arr)

'''
자연수가 있는 배열 arr이 매개변수로 주어지고, 배열 arr안의 숫자들 중에서 앞에 있는 숫자들부터
뒤에 중복 되어 나타나는 숫자들을 중복 횟수를 계산한뒤 중복 횟수만 오름차순으로 배열로 return 하도록 함수를 만들기
만약 중복되는 숫자가 없다면 배열에 -1을 채워서 [-1]을 return 시킨다.
ex) arr=[1,2,3,3,3,3,4,4]에서 3은 4번, 4는 2번 있으므로 [4,2]를 반환한다.
ex2) arr=[3,2,4,4,2,5,2,5,5]에서 2가 3번, 4가 2번, 5가 3번 있으므로 [3,2,3]을 반환한다.
ex3) arr=[3,5,7,9,1]에서 중복해서 나타나는 숫자는 없으므로 [-1]을 반환한다.
'''