# PiPicoXFS5152CE
## Description
XFS5152CE Is a highly integrated speech synthesis chip hat enables Chinese and English speech synthesis. It integrates voice encoding and decoding functions, enabling users to record and play back. In addition, it also integrates innovative lightweight voice recognition, support 30 Command word recognition, and supports the user's command word custom needs.

This is a Micropython library for implementing text-to-speech with the XFS5152CE chip using I2C. It has been tested on Raspberry Pi Pico.

Functitonality other than text-to-speech, such as voice recognition, is not implemented.

Only I2C is supported. SPI or UART are not supported by the library even though the chip supports them.

## Functionality
The library has functionality to send text to the XFS5152CE for voice output.

It also has helper methods to control the output, such as setting language, voice, tone, speed and volume.


## Wiring
* Pin 1 -> GND
* Pin 2 -> 3V3
* Pin 4 -> Speaker +
* Pin 6 -> Speaker -
* Pin 11 -> SCL on Pico (i.e. GPIO5)
* Pin 12 -> SDA on Pico (i.e. GPIO4)

## How to use:
Copy the library (XFS5152CE_I2C.py) to the Pi Pico.

It's really easy to use. Just import, initialize and send the text you want it to speak as follows:
```
# Import the XFS5152CE I2C library
from XFS5152CE_I2C import XFS5152CE

# Initialize the XFS5152CE object with the default I2C pins
xfs = XFS5152CE(scl_pin=5, sda_pin=4)

# Send text to be synthesized and spoken
xfs.speak("Hello!")
```

See XFS5152CE_example.py for more info on how to set the voice, speed, volume and other settings.

## Pinout

![XFS5152CE Module Pinoutt](Documentation/XFS5152CE_Module_Pinout.png)
 
