#!/usr/bin/python
import serial

DEVICE = "/dev/ttyAMA0"
SPEED = 19200

VERSION = "0.1 ALPHA"

EMPHASIZE = 8
DOUBLEHEIGHT = 16
DOUBLEWIDTH = 32

class RPrinter:

    pBold = False
    ser = False
    printSettings = 0b00000000
    

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

	self.ser.write("\n\n\nAnything can happen on Halloween.  Your dog could turn into a smaller dog.")



    def init(self):
        self.ser.write("\x1b\x40")

    def toggleMode(self, mode):
        self.printSettings = self.printSettings ^ mode
        self.ser.write("\x1b\x21" + chr(self.printSettings))

    def println(self, msg):
        self.ser.write(msg + "\n")


printer = RPrinter()


