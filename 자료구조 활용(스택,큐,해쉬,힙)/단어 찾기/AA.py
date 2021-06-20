import sys

sys.stdin = open("input.txt", "r")
n = int(input())
p = {}
for i in range(n):
    word = input()
    p[word] = 1
for i in range(n-1):
    word = input()
    p[word] = 0
for key, val in p.items():
    if val == 1:
        print(key)

'''
시를 쓰기 전에 N개의 단어를 적어둔 노트가 있다.
그리고 시를 쓰는데 N-1개의 단어를 사용했을 때,
시에 사용되지 않은 단어를 찾는 알고리즘이다.
'''

