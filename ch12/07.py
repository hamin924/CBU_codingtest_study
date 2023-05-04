N = input()

length = len(N) #점수 값의 자릿수

sum_left = 0
sum_right = 0

#왼쪽부터 자릿수 더하기
for i in range(length//2):
    sum_left += int(N[i])

#오른쪽 자릿수 더하기
for i in range(length//2, length):
    sum_right += int(N[i])

#왼쪽 자릿수 합과 오른쪽 자릿수 합이 같은지 확인
if sum_left == sum_right:
    print("LUCKY")
else:
    print("READY")
