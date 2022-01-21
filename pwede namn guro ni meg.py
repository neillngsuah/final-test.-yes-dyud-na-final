import serial 
import digitalio
import board
AdruinoSerial = serial.Serial ('COM7',9600)
button_a = digitalio.DigitalInOut(board.BUTTON_A)
button_a.direction = digitalio.Direction.INPUT


led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

SoundSensor = 2 # LM393 Sound Sensor Digital Pin D0 connected to pin 2
LED = 3 # LED connected to pin 3
LEDStatus = False
def setup():
    button_a = digitalio.DigitalInOut(board.BUTTON_A)
    button_a.direction = digitalio.Direction.INPUT
   # pinMode(SoundSensor,INPUT)
    
  #  pinMode(LED,OUTPUT)
    led = digitalio.DigitalInOut(board.D13)
    led.direction = digitalio.Direction.OUTPUT
    #Serial.begin(9600) #initialize serial
while True:

    SensorData = button_a.value
    print(SensorData)
  #  AdruinoSerial.println(SensorData) #print the value
    if SensorData == 1:

        if LEDStatus == False:
            LEDStatus = True
            led.value = True
            #digitalWrite(LED,HIGH)
        elif LEDStatus == True:
            LEDStatus = False
            led.value = False
            #digitalWrite(LED,LOW)


'''AdruinoSerial = serial.Serial ('COM7',9600)
def Sensor(data):
    if Sensor==1:
        if Sensor==False:
            AdruinoSerial('Off')
        elif Sensor==True:
            AdruinoSerial('On')'''
