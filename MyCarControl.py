# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO

class MyCarControl():
    """
    def __init__(self):
        print "init"

    def handle(self, data):
        print data

    def stop():
        print "stop"

    def up():
        print "up"

    def down():
        print "down"

    def left():
        print "left"

    def right():
        print "right"

    """
    def __init__():
		GPIO.setmode(GPIO.BOARD)
		GPIO.setwarnings(False)
		GPIO.setup(11,GPIO.OUT)
		GPIO.setup(12,GPIO.OUT)
		GPIO.setup(15,GPIO.OUT)
		GPIO.setup(16,GPIO.OUT)

    def stop():
        GPIO.output(11, False)
        GPIO.output(12, False)
        GPIO.output(15, False)
        GPIO.output(16, False)

    def up():
        GPIO.output(11, True)
        GPIO.output(12, False)
        GPIO.output(15, True)
        GPIO.output(16, False)

    def down():
        GPIO.output(11, False)
        GPIO.output(12, True)
        GPIO.output(15, False)
        GPIO.output(16, True)

    def left():
        GPIO.output(11, False)
        GPIO.output(12, True)
        GPIO.output(15, True)
        GPIO.output(16, False)

    def right():
        GPIO.output(11, True)
        GPIO.output(12, False)
        GPIO.output(15, False)
        GPIO.output(16, True)
