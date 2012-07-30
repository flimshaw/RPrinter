#!/usr/bin/python
import serial
import textwrap
import markdown
import time
import re

DEVICE = "/dev/ttyAMA0"
SPEED = 19200

VERSION = "0.25 ALPHA"

DEBUG = True

# bytecodes for various printer commands, perhaps soon to be legacy
EMPHASIZE = 8
DOUBLEHEIGHT = 16
DOUBLEWIDTH = 32

CHAR_WIDTH = 30

class RPrinter:

    pBold = False
    ser = False
    printSettings = 0b00000000
    textwrap = textwrap.TextWrapper()

    # Font style byte codes

    # 0 - Font size mode - 12x24 / 16x16 (?)
    # 0 - *
    # 0 - *
    # 0 - Bold
    # |
    # 0 - Double Height
    # 0 - Double Width
    # 0 - *
    # 0 - Underline Mode (?)
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
        if tag in self.printerStyles:
            self.printSettings = self.printSettings ^ self.printerStyles[tag]
            if DEBUG == False:
                self.send("\x1b\x21" + chr(self.printSettings))
            else:
                print "CMD: %s %s" % (tag, self.printSettings)

    # buffers the given string and prints it out to the printer
    def printStr(self, msg):

        html = markdown.markdown(msg)

        p = re.compile(r'(</?[^>]+>)')

        try:
            commandList = p.split(html)
        except NoneType:
            raise

        for cmd in commandList:

            if cmd == '':
                continue

            if cmd[0] == "<" and cmd[-1] == ">":
                # extract the rich innards of our html tag
                tagVal = re.match(r'</?([^>]+)>', cmd).group(1);

                # pass it to our setTypeMode method
                self.setTypeMode(tagVal);
            else:
                self.send(cmd);