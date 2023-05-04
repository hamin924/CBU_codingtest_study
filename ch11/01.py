### ch11은 직관적이게 문제를 해설해서 풀어야함!

n=int(input())
x=list(map(int, input().split())) #input을 공백으로 구분

x.sort()

result = 0 #그룹 수

for i in range(1, len(n)):

    max = x[n-1]
    n -= max
    result+1

print(result)