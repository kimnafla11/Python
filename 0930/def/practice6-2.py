#일회용 패스워드 생성기를 이용하여 3개의 패스워드를 생성하여 출력
#random.choice를 사용
pch = "abcdefghijklmnopqrstuvwxyz0123456789"#나올 수 있는 값 전부 적음
def password() : #함수 생성
    import random #랜덤 임포트
    for num in range(5): #for문으로 비번 5자리수로 만들기
        num+=1
        pw = random.choice(pch) #random.choice를 사용하여 랜덤 값 도출
        print(pw,end="")#출력및 줄 안바꾸기
        
for x in range(3):#비밀번호 세개 반환
    password()#함수 호출
    print()#줄바꿈
