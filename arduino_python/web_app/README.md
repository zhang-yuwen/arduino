```
ipython
In [8]: pwd
Out[8]: '/Users/yuwenzhang/Documents/Arduino/arduino_python/web_app'

import arduino
arduino1=arduino.SerialArduino()
arduino1.start()

arduino1.write("a")
arduino1.write("0")

# LED class
import arduino
led1=arduino.LED()
led1.on()
```