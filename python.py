# Add your Python code here. E.g.
from microbit import *
import radio

radio.on()
radio.config(channel = 13)
#uart.init()

while True:
    ambient_temp = temperature() 
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    z = accelerometer.get_z()
    compx = compass.get_x()
    compy = compass.get_y()
    compz = compass.get_z()
    gesture = accelerometer.current_gesture()
    newmessage = radio.receive()
    if newmessage is not None:
        #display.scroll(newmessage)
        display.show(Image.HAPPY)
        if "TEMPERATURE" in newmessage:
            radio.send('TEMP' + str(ambient_temp) + '\n')
            display.show(Image.HEART)
            
        elif "ACCELEROMETER" in newmessage:
            radio.send('ACC' + str(x) + ' ' + str(y) + ' ' + str(z)+ '\n')
            display.show(Image.HEART)
            
        elif "COMPASS" in newmessage:
            radio.send('COMP' + str(compx) + ' ' + str(compy) + ' ' + str(compz)+ '\n')
            display.show(Image.HEART)
            
        elif "GESTURE" in newmessage:
            radio.send('GES' + str(gesture) + '\n')
            display.show(Image.HEART)
