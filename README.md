# PiPicoXFS5152CE
## Description
XFS5152CE Is a highly integrated speech synthesis chip that enables Chinese and English speech synthesis. It integrates voice encoding and decoding functions, enabling users to record and play back. In addition, it also integrates innovative lightweight voice recognition, support word recognition, and text-to-speech.

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

See Pinout below for the pin layout on the board.

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

## More information
I have included the XFS5152CE datasheet and the development board pinout as PDF documents in the Documentatiton folder if you want to read more about the chip and it's capabilities.

## Dev Board Pinout

![XFS5152CE Module Pinoutt](Documentation/XFS5152CE_Module_Pinout.png)
 
