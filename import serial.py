#install "pip install serial.py" in command prompt 
import serial 
#Change the number of port to connect in arduino
AdruinoSerial = serial.Serial ('COM7',9600)

def Sensor(data):
    if Sensor==1:
    
        if Sensor==False:
            AdruinoSerial('Off')

        elif Sensor==True:
            AdruinoSerial('On')
        

        
