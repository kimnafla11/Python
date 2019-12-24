import RPi.GPIO as GPIO
import time
import pygame #wav 소리 재생을 위한 설정 


pygame.mixer.init() #wav 소리 재생을 위한 설정 
catch = pygame.mixer.Sound("catch.wav") #기울기 센서 감지 시 재생할 음악 지정 

LedBlue = 17 #GPIO 핀 설정 
LedYellow = 27
LedRed = 22
Motor = 18
Tilt = 21
Button = 4

realStudyTime = 0 #실제 공부한 시간 (누적 값)
classCount = 0 #교시 당 학업량, 초기화 되는 공부 시간 

GPIO.setmode(GPIO.BCM) #라즈베리파이 핀 번호를 BCM모드로 사용
GPIO.setup(LedBlue,GPIO.OUT) #빨간 LED를 HiGH(출력)로 사용
GPIO.setup(LedYellow,GPIO.OUT)
GPIO.setup(LedRed,GPIO.OUT)
GPIO.setup(Motor,GPIO.OUT)
GPIO.setup(Tilt,GPIO.IN)
GPIO.setup(Button,GPIO.IN) 

p= GPIO.PWM(Motor, 50)  #PMW:펄스 폭을 50으로 한다.

now ="one" #공부 시간일 시 one, 쉬는 시간일 시 two // 현 상태를 나타내는 변수 

master = input("관리자 암호 설정: ") #스마트 뒤주 관리자 암호 

classNum = int(input("몇교시 공부하시겠습니까?")) #몇 번 반복할 지 지정 
classTime = int(input("1교시 당 몇 분 공부하시겠습니까?")) #한 교시 당 공부할 시간 
breakTime = int(input("1교시 당 쉬는 시간 몇 분으로 하시겠습니까?")) # 한 교시 당 쉬는 시간 

userClass = 0 #실제 반복했던 횟수 선언 

try:
    print("공부 시작")
        
    while True:
            
        if classCount < classTime : #한 교시 공부할 시간이 지나지 않았는 데
            if not (GPIO.input(Tilt)): #기울기 센서 감지 시 
                while True:
                    
                    catch.play(loops=-1) #(loops=-1)노래 소리 무한 반복 
                    print ('====================')
                    print ('=     혼내주세요     =')
                    print ('====================')
                    print ('\n')
                   
                    matching = input("관리자 비밀번호 입력: ") 
                    if(master == matching): #새로 입력한 비밀번호가 관리자 비밀번호와 같을 때 
                        pygame.mixer.pause(); #노래끔
                        break;
                                                        
        if GPIO.input(Button): #의자에 앉아 스위치 깔아뭉갰을때
                
            if now == "one": # 지금 상태가 공부 상태이면 
                GPIO.output(LedRed,True) #빨간불 켜짐
                time.sleep(1)
                classCount +=1 #1초당 한 교시 공부 시간 1씩 증가 
                realStudyTime += 1 #누적 공부 시간 1초당 1씩 증가 
                print("누적 학업시간 : ",realStudyTime)
            
                if classCount == classTime and userClass+1 != classNum : #지정한 한 교시 시간을 채우고 마지막 교시가 아닐 때 
                    now = "two" #현 상태를 쉬는 시간으로 지정 
                    print("쉬는시간")
                    GPIO.output(LedRed,False)
                    userClass += 1 # 실제 반복한 횟수 1씩 증가 
                    
                # 마지막교시처리
                elif classCount == classTime and userClass +1 == classNum: #마지막 교시일 때 
                    userClass += 1
                    
        if now =="two": # 현 상태가 쉬는 시간일 때 
            GPIO.output(LedBlue,True)
            p.start(2.5)#서보모터 움직임 
            p.ChangeDutyCycle(8)#90도
            time.sleep(breakTime)#쉬는 시간 만큼 서보모터 90도 유지 
            print("쉬는시간 끝")
            GPIO.output(LedBlue,False)
            GPIO.output(LedYellow,True)
            time.sleep(1)
            GPIO.output(LedYellow,False)
            p.ChangeDutyCycle(2.5)#지정한 쉬는 시간이 끝나면 서보모터 원위치 
            classCount = 0
                
        if classCount == 0:
                now ="one" #상태를 다시 공부 시간으로 설정 
                    
        if userClass == classNum: #실제 반복 횟수가 지정한 교시 수와 같으면 
            print ('=============목표량 달성==========')
            print("총 공부 시간은",realStudyTime,"분 입니다.ㅎㅎ")
            print ('================================')
            GPIO.cleanup()
            break; #종료 
                    
except KeyboardInterrupt: #예외처리(강제종료시 실행)
    print("\END!!") #end라는 문장 출력
    GPIO.cleanup()
