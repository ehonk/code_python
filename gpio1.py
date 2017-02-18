import time
import RPi.GPIO as GPIO

# RPi.GPIO Layout verwenden (wie Pin-Nummern)
GPIO.setmode(GPIO.BOARD)

# Pin 11 (GPIO 17) auf Output setzen
GPIO.setup(13, GPIO.OUT)

# Dauersschleife
while 1:
  # LED immer ausmachen
  GPIO.output(13, GPIO.LOW)

  time.sleep(5)

  GPIO.output(13, GPIO.HIGH)

  time.sleep(5)
