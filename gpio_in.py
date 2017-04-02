import sys, os
import time
import RPi.GPIO as GPIO

GPIO_IN_PIN = 18

# RPi.GPIO Layout verwenden (wie Pin-Nummern)
GPIO.setmode(GPIO.BOARD)

# Pin 18 (GPIO 24) auf Input setzen
GPIO.setup(GPIO_IN_PIN, GPIO.IN)

# Dauersschleife
while 1:

  # GPIO lesen
  if GPIO.input(GPIO_IN_PIN) == GPIO.HIGH:
    print "GPIO " + str(GPIO_IN_PIN) + " ist high"
  else:
    print "GPIO " + str(GPIO_IN_PIN) + " ist low"
    # Warte 100 ms
    time.sleep(0.2)