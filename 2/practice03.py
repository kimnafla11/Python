#원의 반지름을 입력받아 원의 변적 계산
radius = int(input("원의 반지름을 입력하시오 : "))#input으로 값을 받아 int형으로 변환
PI = 3.141592#원주율은 변하지 않는 값이므로 대문자로
circle = radius**2*PI#원의 넓이를 구하는 공식
print("원의 넓이는 ", circle,"입니다.")#출력

