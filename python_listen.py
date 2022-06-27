# This program checks if an ethernet port is up or down per each blink of  the Arduino LED (TEST)
# and prints a message accordingly.

import os
import time 
import serial

substring = "no" #substring to search for in the output of the command
ser = serial.Serial('/dev/ttyACM0', 9600)   # open serial port

#Check if the serial port is open
if ser.isOpen():
    print("Serial port is open!")
else:
    print ("Please check serial port connection/arduino!")
    exit()

while True: 
    ln = ser.readline() #Read in serial data
    if "Done" in ln.decode('utf-8'): #Check if the string "Done" is in the serial data
        os.system("sudo ethtool enp6s0 | grep Link") #Check if the ethernet port is up or down
        x = os.popen('sudo ethtool enp6s0 | grep Link').read() #Read in the output of the command

        if substring in x: #Check if the string "no" is in the output of the command
            print("Ethernet is down, no connection") #Print the message
    os.system("make -f Makefile")
    # time.sleep()
    # If the user presses Q on the keyboard, exit the program
    keypress = input()
    if keypress == 'q':
        break

    

ser.close()  #Close the serial port
# os.system("./EVTBenchmarkHS")







