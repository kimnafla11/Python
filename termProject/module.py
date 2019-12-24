import RPi.GPIO as GPIO
import time
import sys

LedPin = 22
Sw520dPin = 21

def print_message():
    print ('==================================')
    print ('|            LED Alarm           |')
    print ('|        ----------------        |')
    print ('|        If SW520D Tilt          |')
    print ('|                                |')
    print ('|        LED Will Blink          |')
    print ('|        ----------------        |')
    print ('|                                |')
    print ('|                          OSOYOO|')
    print ('==================================\n')
    print ('Program is running...')
    print ('Please press Ctrl+C to end the program...')
    
    
def setup():
    GPIO.setwarnings(False)
    #set the gpio modes to BCM numbering
    GPIO.setmode(GPIO.BCM)
    #set LedPin's mode to output,and initial level to HIGH(3.3V)
    GPIO.setup(LedPin,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(Sw520dPin,GPIO.IN)

#main function
def main():
    #print info
    print_message()
    while True:
        #read Sw520dPin's level
        if(GPIO.input(Sw520dPin)):
           # GPIO.output(LedPin,GPIO.LOW)
            #time.sleep(0.5)
            #GPIO.output(LedPin,GPIO.HIGH)
            #time.sleep(0.5)
            print ('********************')
            print ('*      안기울어요    *')
            print ('********************')
            print ('\n')
            time.sleep(5)
        else:
            #GPIO.output(LedPin,GPIO.HIGH)
            print ('====================')
            print ('=     움직였어요     =')
            print ('====================')
            print ('\n')
            time.sleep(5)

def destroy():
    GPIO.output(LedPin,GPIO.HIGH)
    GPIO.cleanup()
    
if __name__ == '__main__':
    setup()
    try:
        main()
    except KeyboardInterrupt:
        destroy()