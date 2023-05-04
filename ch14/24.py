N = int(input())

antenna = list(map(int, input().split()))
antenna.sort()

# 중간값 출력
print(antenna[(N-1)//2])