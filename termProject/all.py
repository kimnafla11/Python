import RPi.GPIO as GPIO
import time

LedBlue = 17
LedYellow = 27
LedRed = 22
Motor = 18
Tilt = 21
Button = 4

realStudyTime = 0 #실제 공부한 시간
classCount = 0 #교시 수

GPIO.setmode(GPIO.BCM) #라즈베리파이 핀 번호를 BCM모드로 사용
GPIO.setup(LedBlue,GPIO.OUT) #빨간 LED를 HiGH(출력)로 사용
GPIO.setup(LedYellow,GPIO.OUT)
GPIO.setup(LedRed,GPIO.OUT)
GPIO.setup(Motor,GPIO.OUT)
GPIO.setup(Tilt,GPIO.IN)
GPIO.setup(Button,GPIO.IN) 

p= GPIO.PWM(pin, 50)  #PMW:펄스 폭 변조

try:
    print("START!")

    for classCount in range(1,61): #classCount 1부터 8까지 반복
        if GPIO.input(Button): #의자에 앉아 스위치 깔아뭉갰을때
            time.sleep(1)
            classCount +=1
            if classCount == 50:
                GPIO.output(LedBlue,True)
                p.start(2.5)#원래위치
                p.ChangeDutyCycle(8)#90도

                time.sleep(1)
                classCount+=1
                if classCount == 60:
                    p.ChangeDutyCycle(2.5)#원래 위치로 돌아간다
                    time.sleep(3) 
                    GPIO.output(LedBlue,False)

        
except KeyboardInterrupt: #예외처리(강제종료시 실행)
    print("\END!!") #end라는 문장 출력
    GPIO.cleanup()