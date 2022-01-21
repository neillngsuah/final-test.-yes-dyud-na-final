import serial 
import digitalio
import board
import time 
#Just change any number in COM # to connect with your arduino
AdruinoSerial = serial.Serial ('COM7',9600)
initial = time.monotonic()
previousValue = True
clapCount = 0
#previousTime = millis()

relayoutput = True 

    #Gi off ko lng ang duha ka pinMODE 
sensorpin = digitalio.DigitalInOut(board.D2)
sensorpin.direction = digitalio.Direction.INPUT
    #pinMode(DefineConstants.SENSOR_PIN, INPUT)
relaypin = digitalio.DigitalInOut(board.D3)
relaypin.direction = digitalio.Direction.OUTPUT
    #pinMode(DefineConstants.RELAY_PIN, OUTPUT)

    #Turn off relay . Relay is LOW level triggered relay
#digitalWrite(DefineConstants.RELAY_PIN, HIGH)
relaypin.value = True

while True:
    now = time.monotonic()
    currentValue = sensorpin.value
    if previousValue == True and currentValue == False:
        if clapCount == 1 and now - initial >= 500:
            clapCount = 0

        if clapCount == 0:
            initial = time.monotonic()
        clapCount += 1

        if clapCount == 2:
            relayoutput = not relayoutput
            relaypin.value = relayoutput 
            clapCount = 0
        time.sleep(0.2)
    previousValue = currentValue
