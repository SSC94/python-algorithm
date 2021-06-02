import sys

sys.stdin = open("input.txt","r")
lis = [list(map(int,input().split())) for _ in range(9)]
res = 'YES'
rsp = csp = 0
rep = cep = 3

for i in range(9):
    tmpSquare = list([0] * 10)
    tmpRow = list([0] * 10)
    tmpColumn = list([0] * 10)

    for j in range(9):
        tmpRow[lis[i][j]] = 1
        tmpColumn[lis[j][i]] = 1

    for r in range(rsp,rep):
        for c in range(csp,cep):
            tmpSquare[lis[r][c]] = 1

    if sum(tmpRow) != 9 or sum(tmpColumn) != 9 or sum(tmpSquare) != 9:
        res = 'NO'

    if cep < 9:
        csp += 3
        cep += 3
    else:
        csp = 0
        cep = 3
        rsp += 3
        rep += 3

print (res)

'''
주어진 9X9 스도쿠를 원래 스도쿠 규칙인 가로, 세로, 3X3칸에 1~9까지 중복없이 있는지
확인하여 만약 올바른 스도쿠면 'YES'를 출력하고, 그렇지 않으면 'NO'를 출력하는 알고리즘이다.

리스트 lis에 9X9스도쿠 숫자들을 저장한다. 그리고, 결과를 보여주는 res를 'YES'로 초기 할당한다.
rsp,rep,csp,cep는 스도쿠의 3X3칸을 검사할 포인터들로 rsp는 행의 시작점, rep는 행의 끝점,
csp는 열의 시작점, cep는 열의 끝점이다. 그리고 검사는 총 3가지로 3X3칸, 행 9칸, 열 9칸이다.
for문 아래 tmp리스트 3개는 각각 검사 3가지에 사용될 리스트들로 1~9까지 하나씩 존재 해야 하니
검사중에 나온 1~9사이 숫자를  tmp의 인덱스로 받아 값을 +1한다. 그 후에 첫번째 if문으로 
어느 하나라도 tmp리스트들의 요소합이 9가 아니면 res를 'NO'로 변경한다. 왜냐하면 스도쿠는 1~9사이의
숫자가 한번씩만 나오므로 정상적인 스도쿠라면 각 tmp들의 인덱스0을 제외한 나머지에는 값이 1이고,
이 값들을 모두 더하면 9가 나오기 때문이다. 두 번째 if문은 3X3칸을 검사할 때 사용하는 포인터들을
이동시켜서 최종적으로 9번 검사한다.
'''

