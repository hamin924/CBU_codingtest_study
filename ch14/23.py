N = int(input())

students=[] #학생 정보 담을 리스트

for i in range(N):
    students.append(input().split()) #N의 개수만큼 입력 받아서 배열에 넣음

# key 값으로 국어는 감소, 영어는 증가, 수학은 감소
students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0])) #이 부분 이해가 잘 안돼

for student in students:
    print(student[0])
