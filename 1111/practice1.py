import RPi.GPIO as GPIO #RPi.GPIO 모듈을 GPIO란 이름으로 사용
import time #time함수 사용

LED_RED=17 # 빨간 LED를 GPIO17번에 연결
LED_YELLOW=27 # 노랑 LED를 GPIO27번에 연결
LED_GREEN=22 #초록 LED를 GPIO22번에 연결

BUTTON=6 # 스위치 GPIO6번에 연결

GPIO.setmode(GPIO.BCM) #라즈베리파이 핀 번호를 BCM모드로 사용
GPIO.setup(LED_RED,GPIO.OUT) #빨간 LED를 HiGH(출력)로 사용
GPIO.setup(LED_YELLOW,GPIO.OUT)
GPIO.setup(LED_GREEN,GPIO.OUT)
GPIO.setup(BUTTON,GPIO.IN) 

now="green" #지금 상태를 표시하는 String now변수선언 후 green값 저장

try:
    print("START!")
    while True:
        
        if GPIO.input(BUTTON):#버튼이 눌렸을때 실행
            
            if  now == "green" :  #now변수 값이 green이면 아래 문장 실행
                GPIO.output(LED_GREEN,True) #디지털 출력을 HIGH로 설정
                GPIO.output(LED_YELLOW,False) #디지털 출력을 LOW로 설정-LED끔
                GPIO.output(LED_RED,False) #디지털 출력을 LOW로 설정-LED끔
                now = "yellow" # 지금 상태를 표시하는 변수에 yellow값 저장
            

            elif now =="yellow": #now변수 값이 yellow이면 아래 문장 실행
                 GPIO.output(LED_GREEN,False) #디지털 출력을 LOW로 설정 - 초록불 끔
                 GPIO.output(LED_YELLOW,True) #디지털 출력을 HIGH로 설정 - 노란불 킴
                 time.sleep(1) #1초동안 노란불 지
                 GPIO.output(LED_YELLOW,False)# 노란불 끔
                 GPIO.output(LED_RED,True)#디지털 출력을 HIGH로 설정 - 빨간불 킴
                 now="green" #now변수에 green값을 저장
        
            time.sleep(1) #스위치 디지털 출력을 1초 지연시킴
            
except KeyboardInterrupt: #예외처리(강제종료시 실행)
    print("\END!!") #end라는 문장 출력
    GPIO.output(LED_RED,False) #모든 LED 디지털 출력을 LOW로 설정
    GPIO.output(LED_YELLOW,False)
    GPIO.output(LED_GREEN,False)
    GPIO.cleanup()
