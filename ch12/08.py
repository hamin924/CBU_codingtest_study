S = input()

#결과 배열
result = []
#숫자 합
sum = 0

for i in S:
    if i.isalpha():
        result.append(i)
    else:
        sum += int(i)

result.sort()

if sum != 0:
    result.append(str(sum))

print(''.join(result))