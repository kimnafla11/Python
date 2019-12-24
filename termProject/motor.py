
import RPi.GPIO as GPIO
import time

pin =18


def my_left():
    p.ChangeDutyCycle(5)
def my_middle():
    p.ChangeDutyCycle(7.5)
def my_right():
    p.ChangeDutyCycle(12.5)


GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
p= GPIO.PWM(pin, 50)  #PMW:펄스 폭 변조
p.start(2.5)#원래위치
p.ChangeDutyCycle(8)#90도
time.sleep(3)
p.ChangeDutyCycle(2.5)#원래 위치로 돌아간다
time.sleep(3)
#time.sleep(5)
#my_left()
#time.sleep(5)
#my_right()
#time.sleep(5)
#my_middle()
#time.sleep(5)

cnt = 0

#try:

    #while True:
        #p.ChangeDutyCycle(12.5) #최댓값
        #time.sleep(1)
        #p.ChangeDutyCycle(10.0)
        #time.sleep(1)
        #p.ChangeDutyCycle(7.5) #0
        #time.sleep(1)
        #p.ChangeDutyCycle(5.0)
        #time.sleep(1)
        #p.ChangeDutyCycle(2.5) #최솟값
        #time.sleep(1)

#except KeyboardInterrupt:
    #p.stop()
    #GPIO.cleanup()