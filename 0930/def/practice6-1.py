#일회용 패스워드 생성기를 이용하여 3개의 패스워드를 생성하여 출력
#random.randrange()를 사용
pch = "abcdefghijklmnopqrstuvwxyz0123456789"#나올수 있는 값 다 적기
def password() :#함수 생성
    import random#랜덤 임포트
    for num in range(5): #5번 반복 (5자리 비밀번호)
        num+=1 
        pw = pch[random.randrange(0,35)] #pch의 인덱스 번호 범위 지정
        print(pw,end="")#pw출력 줄바꿈 안되게
        
for x in range(3):#비밀번호 3개 생성
    password()#함수 호출
    print()#줄바꿈
