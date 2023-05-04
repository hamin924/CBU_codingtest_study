N = int(input())

data=[]

for i in range(N): #N개의 개수만큼 입력받기
    data.append(int(input()))

data.sort(reverse=True) # %값 왜 출력돼...?


for i in data:
    print(i, end=' ')