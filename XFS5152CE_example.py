from XFS5152CE_I2C import XFS5152CE
import time

# Initialize the XFS5152CE object with the default I2C pins
xfs = XFS5152CE(scl_pin=5, sda_pin=4)

# Send text to be synthesized and spoken
xfs.speak("Hello!")
# Wait for some time to ensure the speech synthesis is complete
time.sleep(1)

#Set the voice to male. Possible values are: female1|female2|male1|male2|cartoon|girl
xfs.set_voice("male1")
xfs.speak("I now have a male voice!")
time.sleep(2)

xfs.set_voice("female2")
xfs.speak("You can also set tone, volume, speed etc, see the library file on how to use them.")

time.sleep(10)

# Optionally stop the speech synthesis explicitly (useful if text is long)
xfs.stop()

# Query and print chip status (optional)
status = xfs.query_status()
print("Chip status:", status)