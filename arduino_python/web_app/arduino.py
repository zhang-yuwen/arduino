#import serial
#ser = serial.Serial('/dev/cu.usbmodem1201')  
#print(ser.name)         
#ser.write(bytes("x", 'utf-8'))
#value = ser.readline() # reads from buffer until new line
#print(value)          
#ser.close()             

# Importing Libraries
import serial
import serial.tools.list_ports
import time
import threading
from time import sleep


ON = "a"
OFF = "0"

class SerialArduino():
    def __init__(self) -> None:
        self.output_buffer = []
        self.input_buffer = []
        self.serial_ports = serial.tools.list_ports.comports()
        self.arduino = serial.Serial(self.serial_ports[1].device, timeout=0.01)

    def write(self, message):
        self.output_buffer.append(message)
    
    def read(self):
        return self.input_buffer.pop(0,None)

    def start(self):
        thread1 = threading.Thread(target=self.run)
        thread1.start()

    def run(self):
        while True:
            # Write to output_buffer
            if self.output_buffer:
                message = self.output_buffer.pop(0) 
                self.arduino.write(bytes(message, 'utf-8'))
            # Read 
            data = self.arduino.readline().strip()
            if data:
                self.input_buffer.append(data)

class LED():
    def __init__(self) -> None:
        self.led_state = False
        self.arduino = SerialArduino()

    def on():
        

    def off():


def led_on():
    global output_buffer
    output_buffer.append(ON)

def led_off():
    global output_buffer
    output_buffer.append(OFF)


if __name__ == "__main__":
    thread1 = threading.Thread(target=serial_io)
    thread2 = threading.Thread(target=control)

    thread1.start()
    thread2.start()