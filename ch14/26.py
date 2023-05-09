# 힙 정렬로 풀어야함!

import heapq

n = int(input())

heap=[]

for i in range(n): #N개의 개수만큼 입력받기
    data=int(input())
    heapq.heappush(heap, data)

result = 0 # 최소한 몇번의 비교가 필요한지 결괏값

while len(heap) != 1: # 힙에 원소가 1개 남을 때 까지
    # 가장 작은 2개의 카드 묶음 꺼내기
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    # 카드 묶음을 합쳐서 다시 삽입
    sum_value = one+two
    result += sum_value
    heapq.heappush(heap,sum_value)

print(result)
