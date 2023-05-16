# 이진탐색 소스 코드 구현(재귀 함수)

def binary_search(array, start, end):
    if start > end:
        return None
    mid = (start+end) //2
    if array[mid] == mid: # 고정점을 찾은 경우 인덱스 반환
        return mid
    elif array[mid] > mid:
        return binary_search(array, start, mid - 1)
    else:
        return binary_search(array, mid + 1, end)

n = int(input())

array=list(map(int,input().split()))

index = binary_search(array, 0, n-1)

if index == None: # 고정점이 없는 경우 -1 출력
    print(-1)
else:
    print(index)