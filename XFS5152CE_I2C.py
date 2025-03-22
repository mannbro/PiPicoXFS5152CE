from machine import I2C, Pin
import time

class XFS5152CE:
    DEFAULT_I2C_ADDR = 0x40  # Default I2C address, adjust if different

    def __init__(self, scl_pin=5, sda_pin=4, freq=20000):
        self.i2c = I2C(0, scl=Pin(scl_pin), sda=Pin(sda_pin), freq=freq)
        #Default to English
        self.set_pronounciation("words")
        self.set_language("english")

# Use Tone (boolean)
# Values: True|False    
    def set_use_tone(self, value):
        if(value):
            self.speak("[x1]")
        else:
            self.speak("[x0]")

# Set Tone (int)
# Values: 0-10
    def set_tone(self, value):
        if(1 <= value <= 10):
            self.speak(f"[x{value}]")

# Set Volume (int)
# Values: 0-10
    def set_volume(self, value):
        if(1 <= value <= 10):
            self.speak(f"[v{value}]")

# Set Speed (int)
# Values: 0-10
    def set_speed(self, value):
        if(1 <= value <= 10):
            self.speak(f"[s{value}]")

# Set Voice (string)
# Values: female1|female2|male1|male2|cartoon|girl
    def set_voice(self, value):
        if(value=="female1"):
            self.speak("[m3]")
        elif(value=="female2"):
            self.speak("[m53]")
        elif(value=="male1"):
            self.speak("[m51]")
        elif(value=="male2"):
            self.speak("[m52]")
        elif(value=="cartoon"):
            self.speak("[m54]")
        elif(value=="girl"):
            self.speak("[m55]")

# Set Language (string)
# Values: auto|chinese|english
    def set_language(self, value):
        if(value=="chinese"):
            self.speak("[g1]")
        elif(value=="english"):
            self.speak("[g2]")
        else:
            self.speak("[g0]")

# Set Pronounciation (string)
# Values: auto|letters|words
    def set_pronounciation(self, value):
        #Example: Hello -> H-E-L-L-O
        if(value=="letters"):
            self.speak("[h1]")
        #Example: Hello -> Hello
        elif(value=="words"):
            self.speak("[h2]")
        else:
            self.speak("[h0]")

# Set Numbers (string)
# Values: auto|digits|cardinal
    def set_numbers(self, value):
        #Example: 123 => One Two Three
        if(value=="digits"):
            self.speak("[n1]")
        #Example: 123 => Onehundred and twenty three
        elif(value=="cardinals"):
            self.speak("[n2]")
        else:
            self.speak("[n0]")

    def speak(self, text):
        data_length = len(text) + 2  # command_code + parameter byte
        header = bytes([
            0xFD,
            (data_length >> 8) & 0xFF,  # Data length high byte
            data_length & 0xFF,         # Data length low byte
            0x01,                       # Speech synthesis command
            0x00                        # Parameter (Encoding=UTF)
        ])
        data = header + text
        print("Sending I2C data:", data)
        try:
            self.i2c.writeto(self.DEFAULT_I2C_ADDR, data)
            print("Data sent successfully.")
        except OSError as e:
            print("I2C error:", e)
        time.sleep(0.1)

    def stop(self):
        command = bytes([0xFD, 0x00, 0x02, 0x02])
        self.i2c.writeto(self.DEFAULT_I2C_ADDR, command)

    def pause(self):
        command = bytes([0xFD, 0x00, 0x02, 0x03])
        self.i2c.writeto(self.DEFAULT_I2C_ADDR, command)

    def resume(self):
        command = bytes([0xFD, 0x00, 0x02, 0x04])
        self.i2c.writeto(self.DEFAULT_I2C_ADDR, command)

    def query_status(self):
        command = bytes([0xFD, 0x00, 0x02, 0x21])
        self.i2c.writeto(self.DEFAULT_I2C_ADDR, command)
        time.sleep(0.1)
        status = self.i2c.readfrom(self.DEFAULT_I2C_ADDR, 1)
        return status
