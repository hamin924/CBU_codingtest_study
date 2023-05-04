N = int(input())

students=[] #학생 정보 담을 리스트

for i in range(N):
    students.append(input().split()) #N의 개수만큼 입력 받아서 배열에 넣음

students.sort(key=lambda student: student[1])

for i in students:
    print(i[0], end=' ')