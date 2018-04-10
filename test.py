import serial
import sys
import io
import os

baudrate_list = [50, 75, 110, 134, 150, 200, 300, 600, 1200, 1800, 2400, 4800, 9600, 19200, 38400, 57600, 115200]

class serial_mod():

    def __init__(self):
        self.port = "com6"
        self.baudrate = 115200
        self.method = "both"
        self.location = os.getcwd()
        self.log_file = "serial_log.txt"
        self.target = []

    def port_select(self, port):
        self.port = port

    def op_mode(self, method):
        if method == "console":
            print "display serial log on the console"
            self.method = "console"
        elif method == "log":
            print "save serial log in the log file: " + self.location + "\\" + self.log_file
            self.method = "log"
        elif method == "no":
            print "no output on console and log file."
            self.method = "no"
        elif method == "both":
            print "display serial log on console and log in log file" + self.location + "\\" + self.log_file
            self.method = "both"
        else:
            print "Enter currect method: 'console', 'log' or 'both'"

    def console_(self, ser):
        while(ser.isOpen()):
            while 1:
                bytes = ser.readline()
                print bytes
                for temp in self.target:
                    if temp in bytes:
                        print "find " + temp
                        ser.close()
                        break

    def no_(self,ser):
        while(ser.isOpen()):
            while 1:
                bytes = ser.readline()
                for temp in self.target:
                    if temp in bytes:
                        print "find " + temp
                        ser.close()
                        break

    def both_(self,ser):
        log_fp = open(self.location +"\\"+ self.log_file ,"a")
        while(ser.isOpen()):
            while 1:
                bytes = ser.readline()
                print bytes
                log_fp.write(bytes)
                for temp in self.target:
                    if temp in bytes:
                        print "find " + temp
                        ser.close()
                        log_fp.close()
                        break

    def log_(self, ser):
        log_fp = open(self.location + "\\" + self.log_file, "a")
        while(ser.isOpen()):
            while 1:
                bytes = ser.readline()
                print bytes
                log_fp.write(bytes)
                for temp in self.target:
                    if temp in bytes:
                        print "find " + temp
                        ser.close()
                        log_fp.close()
                        break

    def read_keyword(self):
        try:
            tar_fp = open("target.txt", "r")
            while tar_fp != EOFError():
                self.target.append(tar_fp.read().strip())
            tar_fp.close()
        except:
            print "no such file target.txt"

    def keyword(self, keyword):
        self.target.append(keyword)

    def clean_keyword(self):
        del self.target[:]
        self.target = []

    def set_baudrate(self, baudrate):
        if baudrate in baudrate_list:
            self.baudrate = baudrate

    def log_loc(self, location):
        self.location = location

    def help(self):
        print "This class is for serial log display on console or log to file"

    def find(self):
        ser = serial.Serial(self.port, baudrate=self.baudrate)
        try:
            ser.isOpen()
            print("serial port com", sys.argv[1])
        except:
            print("can't open serial port.")
        if self.op_mode == "console":
            self.console_(ser)
        elif self.op_mode == "no":
            self.no_(ser)
        elif self.op_mode == "both":
            self.both_(ser)
        elif self.op_mode == "log":
            self.log_(ser)

    def show_settings(self):
        print "port : " + self.port 
        print "baudrate : " + self.baudrate 
        print "method : " + self.method 
        print "save location : " + self.location + "\\" + self.log_file
        print "find : " + self.target

if __name__ == "__main__":
    print "test"
