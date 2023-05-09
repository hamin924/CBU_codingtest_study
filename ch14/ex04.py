n, k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort() # 배열 A 오름차순으로 정렬
b.sort(reverse=True) # 배열 B 내림차순으로 정렬

for i in range(k):
    if a[i] < b[i]: # a의 원소가 b의 원소보다 작은 경우
        a[i], b[i] = b[i], a[i] # 두 원소 교체
    else: # ㅁ의 원소가 b의 원소보다 크거나 같을 경우 반복문 탈출
        break

print(sum(a))