#!/usr/bin/python
import serial
import textwrap
import markdown
import time

DEVICE = "/dev/ttyAMA0"
SPEED = 19200

VERSION = "0.25 ALPHA"

DEBUG = True

EMPHASIZE = 8
DOUBLEHEIGHT = 16
DOUBLEWIDTH = 32

CHAR_WIDTH = 30

class RPrinter:

    pBold = False
    ser = False
    printSettings = 0b00000000
    textwrap = textwrap.TextWrapper()

    printerStyles = {
        'strong': 8,
        'h1': 48,
        'h2': 16,
        'h3': 32
    }
    
    def __init__(self):

        if DEBUG == False:
            try:
                self.ser = serial.Serial(DEVICE, SPEED)
            except serial.serialutil.SerialException:
                print "Error opening serial port! Perhaps you don't have permission?  Deadbeat."
                exit()

            self.init()
        else:
            print "hello"

    def init(self):

        # send the printer initialization code
        self.send("\x1b\x40")

        # initialize our text textwrap
        self.textwrap.width = CHAR_WIDTH
        self.textwrap.break_on_hyphens = True

        self.send("\n\n")

    def send(self, data):
        if DEBUG == False:
            self.ser.write(data)
        else:
            print str(data)

    def setTypeMode(self, tag):
        if tag in printerStyles:
            self.printSettings = self.printSettings ^ mode
            if DEBUG == False:
                self.send("\x1b\x21" + chr(self.printSettings))
            else:
                print tag

    # buffers the given string and prints it out to the printer
    def printStr(self, msg):

        html = markdown.markdown(msg)

        print html

        # break the text into an array of lines
        #bufferedText = self.textwrap.wrap(msg)

        #for line in bufferedText:
        #    self.println(line)

    def printChar(self, msg):
        self.send(msg)

    def println(self, msg):
        self.printChar(msg + "\n")
        time.sleep(.5)