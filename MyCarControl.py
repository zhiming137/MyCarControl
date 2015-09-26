# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO

class MyCarControl():
    """
    def __init__(self):
        print "init"

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
    def __init__(self):
		GPIO.setmode(GPIO.BOARD)
		GPIO.setwarnings(False)
		GPIO.setup(11,GPIO.OUT)
		GPIO.setup(12,GPIO.OUT)
		GPIO.setup(15,GPIO.OUT)
		GPIO.setup(16,GPIO.OUT)

    def handle(self, data):
        if data == 'up':
            self.up()
        elif data == 'down':
            self.down()
        elif data == 'left':
            self.left()
        elif data == 'right':
            self.right()
        else:
            self.stop()


    def stop(self):
        GPIO.output(11, False)
        GPIO.output(12, False)
        GPIO.output(15, False)
        GPIO.output(16, False)

    def up(self):
        GPIO.output(11, True)
        GPIO.output(12, False)
        GPIO.output(15, True)
        GPIO.output(16, False)

    def down(self):
        GPIO.output(11, False)
        GPIO.output(12, True)
        GPIO.output(15, False)
        GPIO.output(16, True)

    def left(self):
        GPIO.output(11, True)
        GPIO.output(12, False)

    def right(self):
        GPIO.output(15, True)
        GPIO.output(16, False)

