import serial #Serial imported for Serial communication
import time #Required to use delay functions


def main():
    
    
    ArduinoSerial = serial.Serial('COM3',9600)
    time.sleep(2)
    print (ArduinoSerial.readline())

    while(1):
        var = '1' #get input from user
     
   
        if (var == '1'): #if the value is 1
            ArduinoSerial.write(str.encode('1'))
            print ("LED turned ON")
            time.sleep(1)
        break
main()           
            