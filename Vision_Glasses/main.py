import RPi.GPIO as GPIO
import time

GPIO. setmode(GPIO.BCM)
GPIO.setwarnings(False)

# GPIO pin 번호 설정
sensor=17
sound=18
led_red=20
led_green=21

# GPIO포트 세팅
GPIO.setup(sensor, GPIO.IN)
GPIO.setup(sound, GPIO.OUT)
GPIO.setup(led_red, GPIO.OUT)
GPIO.setup(led_green, GPIO.OUT)

# PWM 객체 생성
p = GPIO.PWM(sound, 1000)  

# 부저 메소드
def paly_sound():
    p.start(0)
    p.ChangeFrequency(550) #주파수 50hz 기본으로 하면 시끄러워서 50으로 지정, 기존 390,195,550 조정해보기
    p.ChangeDutyCycle(10)
    time.sleep(0.5)
    p.ChangeDutyCycle(0)
    time.sleep(0.2)
    p.stop()
    
print("sensor operating~")
time.sleep(2)
#센서 동작 라인 
try:
    while True:
        if GPIO.input(sensor)==1:
            GPIO.output(led_red, 1)            
            GPIO.output(led_green, 0)
            paly_sound()
            print("motion detect")
            #time.sleep(0.5)
        elif GPIO.input(sensor)==0:
            GPIO.output(led_red, 0)
            GPIO.output(led_green, 1)
            time.sleep(0.5)
except KeyboardInterrupt:
    print("stop")
    GPIO.cleanup()
    
    