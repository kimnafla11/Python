#gipo_pir_sensor.py
import RPi.GPIO as GPIO #RPi.GPIO 모듈을 GPIO란 이름으로 사용
import time #time함수 사용

PIR = 6 #PRI센서를 GPIO 6번에 연결
LED = 17#LED를 GPIO 17번에 연결

GPIO.setmode(GPIO.BCM)#라즈베리파이 핀 번호를 BCM모드로 사용
GPIO.setup(PIR,GPIO.IN)#PIR 센서를 High(출력)로 사용
GPIO.setup(LED,GPIO.OUT)#LED 를 High(출력)로 사용
GPIO.output(LED,False)#LED 처음 디지털 출력을 LOW로 설정
while True:
    time.sleep(3)
    if not GPIO.input(PIR): # PIR센서가 적외선을 감지하면
        print("Motion Detected!!!") #문장 실행
        GPIO.output(LED,True) #Led 디지털출력 HIGH로 설정
    elif GPIO.input(PIR): #PIR센서가 적외선을 감지하지않으면
        GPIO.output(LED,False) #LED 디지털출력을 LOW로 설정
