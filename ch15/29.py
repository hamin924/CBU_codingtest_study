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


n, c = map(int,input().split())

array = [] # 집 좌표 정보 저장하는 배열

for i in range(n):
    array.append(int(input()))

array.sort()

start = array[1] - array[0] # 집의 좌표 중에 가장 작은 값
end = array[-1] - array[0] # 집의 좌표 중에 가장 큰 값

result = binary_search(array, start, end)

print(result)