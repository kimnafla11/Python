#이름과 나이 입력하게하고 현재년도를 기준으로 100살이 되는 연도 출력
name = input("이름을 입력하시오 : ")
age = int(input("나이를 입력하시오 : "))
nowYear = 2019#현재 년도
year = (nowYear-age)+100 #100살이 되는 해
print(name," 님은 ",year,"년에 백살이시네요!")
