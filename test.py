import serial
import sys
import io
import os

class serial_port():
    def __init__(self, port_Num):
        self.serialport = "com" + port_Num
       
        
    def log_and_find(self):
        ser = serial.Serial(self.serialport, baudrate=115200)
        try:
            ser.isOpen()
            print("serial port ", self.serialport)
        except:
            print("can't open serial port.")
        if (os.path.isfile("log.txt") == 1):
            os.remove("log.txt")
        fp = open("log.txt", "a")
        tar_fp = open("target.txt", "r")
        target = tar_fp.read().strip()
        print "Searching for " + ": " + target
        tar_fp.close()
        if(ser.isOpen()):
            while 1:
                bytes = ser.readline()
                fp.write(bytes)
                if target in bytes:
                    print "find " + target
                    ser.close()
                    fp.close()
                    break


if __name__ == "__main__":
    test = serial_port(sys.argv[1]).log_and_find()
