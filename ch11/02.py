S = input()

result = int(S[0]) # 첫번째 숫자로 인식

for i in range(1, len(S)):
    num = int(S[i]) #i번째 숫자 num
    if num <=1 or result<=1:
        result += num
    else:
        result *= num

print(result)