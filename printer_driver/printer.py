#!/usr/bin/python
import serial
import textwrap
import time

DEVICE = "/dev/ttyAMA0"
SPEED = 19200

VERSION = "0.25 ALPHA"

EMPHASIZE = 8
DOUBLEHEIGHT = 16
DOUBLEWIDTH = 32

CHAR_WIDTH = 32

class RPrinter:

    pBold = False
    ser = False
    printSettings = 0b00000000
    textwrap = textwrap.TextWrapper()
    
    def __init__(self):
        try:
            self.ser = serial.Serial(DEVICE, SPEED)
        except serial.serialutil.SerialException:
            print "Error opening serial port! Perhaps you don't have permission?"
            exit()

        self.init()
        self.toggleMode(DOUBLEHEIGHT)
        self.ser.write("\nNo Pants Island!\n")
        self.toggleMode(DOUBLEHEIGHT)
        self.ser.write("Version " + VERSION + "\n\n")
        self.printStr("Cras mattis consectetur purus sit amet fermentum. Nulla vitae elit libero, a pharetra augue. Cras mattis consectetur purus sit amet fermentum. Nulla vitae elit libero, a pharetra augue.")

    def init(self):
        
        # send the printer initialization code
        self.ser.write("\x1b\x40")

        # initialize our text textwrap
        self.textwrap.width = CHAR_WIDTH
        self.textwrap.break_on_hyphens = True


    def toggleMode(self, mode):
        self.printSettings = self.printSettings ^ mode
        self.ser.write("\x1b\x21" + chr(self.printSettings))

    # buffers the given string and prints it out to the printer
    def printStr(self, msg):

        # break the text into an array of lines
        bufferedText = self.textwrap.wrap(msg)

        for line in bufferedText:
            self.println(line)

    def println(self, msg):
        self.ser.write(msg + "\n")
        time.sleep(.1)