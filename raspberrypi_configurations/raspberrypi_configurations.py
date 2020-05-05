#----------------------------------BUZZER INITIALIZER-------------------------------


import pigpio

# create an instance of the pigpio library

pi = pigpio.pi()

# define the pin used by the Buzzer. This is GPIO12, which is pin 32
buzzer = 12

is_buzzer_off = True
is_buzzer_used_locally = False


#----------------------------------RGB LED INITIALIZER-------------------------------
import time
import RPi.GPIO as GPIO  # we import the RPi.GPIO library with the name of GPIO

redled = 8
greenled = 10
blueled = 12

GPIO.setmode(GPIO.BOARD) #we set the pin numbering to the GPIO.BOARD numbering

GPIO.setup(redled, GPIO.OUT) #we set the PIN8 as a output pin
GPIO.setup(greenled, GPIO.OUT) #we set the PIN10 as a output pin
GPIO.setup(blueled, GPIO.OUT) #we set the PIN12 as a output pin

redPWM = GPIO.PWM(redled, 1000)  # we create a PWM instance on the 8th pin that is set as an output.
greenPWM = GPIO.PWM(greenled, 1000)  # we create a PWM instance on the 10th pin that is set as an output.
bluePWM = GPIO.PWM(blueled, 1000)  # we create a PWM instance on the 12th pin that is set as an output.

# we start the pwm pins with a duty cycle of 0. This means that at first the pins
# have an output of a digital 0.
redPWM.start(0)
greenPWM.start(0)
bluePWM.start(0)


def rgb_led_configure(red_duty_cycle=0, green_duty_cycle=0, blue_duty_cycle=0):
    redPWM.ChangeDutyCycle(red_duty_cycle)
    greenPWM.ChangeDutyCycle(green_duty_cycle)
    bluePWM.ChangeDutyCycle(blue_duty_cycle)


def rgb_turn_off():
    rgb_led_configure(red_duty_cycle=0, green_duty_cycle=0, blue_duty_cycle=0)


def start_rgb_led_by_note(musical_note):
    if musical_note == 'c':
        rgb_led_configure(red_duty_cycle=100)  #red
    elif musical_note == 'cs':
        rgb_led_configure(green_duty_cycle=40, blue_duty_cycle=20) # pale cyan
    elif musical_note == 'd':
        rgb_led_configure(red_duty_cycle=100, green_duty_cycle=100)  #yellow
    elif musical_note == 'ds':
        rgb_led_configure(red_duty_cycle=25, blue_duty_cycle=60)  #pale magenta
    elif musical_note == 'e':
        rgb_led_configure(green_duty_cycle=100)  #green
    elif musical_note == 'f':
        rgb_led_configure(green_duty_cycle=100, blue_duty_cycle=100)   #cyan
    elif musical_note == 'fs':
        rgb_led_configure(red_duty_cycle=100, green_duty_cycle=3)   #orange
    elif musical_note == 'g':
        rgb_led_configure(blue_duty_cycle=100)  #blue
    elif musical_note == 'gs':
        rgb_led_configure(red_duty_cycle=60, green_duty_cycle=40)  #pale yellow
    elif musical_note == 'a':
        rgb_led_configure(blue_duty_cycle=100, red_duty_cycle=100)  #magenta
    elif musical_note == 'as':
        rgb_led_configure(blue_duty_cycle=70, green_duty_cycle=20)  #pale blue
    elif musical_note == 'b':
        rgb_led_configure(red_duty_cycle=100, green_duty_cycle=100, blue_duty_cycle=100)  #white


#----------------------------------BUTTONS INITIALIZER-------------------------------
# define the pins used by the buttons
# these are pin numbers
button3 = 18
button2 = 24
button1 = 26

# set the pins for the buttons as INPUT, and we will
# set the initial value to On, or we can say that will be pulled up
GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
