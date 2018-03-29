import serial
import sys
import io
import os

baudrate_list = [50, 75, 110, 134, 150, 200, 300, 600, 1200, 1800, 2400, 4800, 9600, 19200, 38400, 57600, 115200]

class serial_mod():

    def __init__(self, port_Num):
        self.port = "com6"
        self.baudrate = 115200
        self.method = "both"
        self.location = os.getcwd()
        self.log_file = "serial_log.txt"
        tar_fp = open("target.txt", "r")
            while tar_fp != EOFError():
                self.target.append() = tar_fp.read().strip()
        tar_fp.close()

    def port_select(self, port):
        self.port = port

    def op_mode(self, method):
        if method == "console":
            print "display serial log on the console"
            self.method = "console"
        elif method == "log":
            print "save serial log in the log file: " + self.location + "\\" + self.log_file
            self.method = "log"
        elif method == "no"
        elif method == "both":
            self.method = "both"
        else:
            print "Enter currect method: 'console', 'log' or 'both'"
    def keyword_file(self, )
    def keyword(self, keyword):
        self.target = keyword

    def set_baudrate(self, baudrate):
        if baudrate in baudrate_list:
            self.baudrate = baudrate

    def log_loc(self, location):
        self.location = location

    def help(self):
        
if __name__ == "__main__":
    print("alone")
