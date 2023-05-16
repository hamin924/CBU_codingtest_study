n, m = map(int,input().split()) # 떡의 개수 n 과 요청한 떡의 길이 m 을 입력받기

array=list(map(int,input().split())) # 각 떡의 개별 높이 정보를 입력받기

start = 0
end = max(array)

result = 0
while(start <= end):
    total = 0
    mid = (start+end)//2
    for i in array: # 잘랐을 때의 떡의 양 계산
        if i > mid:
            total += i - mid
    if total < m: # 떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
        end = mid - 1
    else: # 떡의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색)
        result = mid
        start = mid + 1

print(result)