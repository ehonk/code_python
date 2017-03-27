#!/usr/bin/env python
# -*- coding: utf-8 -*-
#title           :menu.py
#description     :This program displays an interactive menu on CLI
#author          :
#date            :
#version         :0.1
#usage           :python menu.py
#notes           :
#python_version  :2.7.6  
#=======================================================================
 
# Import the modules needed to run the script.
import sys, os
import time
import RPi.GPIO as GPIO

relaisGPIO = 13
offTime = 90
onTime = 30
counter = 0
 
# Main definition - constants
menu_actions  = {}  
 
# =======================
#     MENUS FUNCTIONS
# =======================
 
# Main menu
def main_menu():
    # os.system('clear')
    
    print "Bavarian Engineering Relais Timer by AM 2017"
    print "Ontime: " + str(onTime) + " seconds -  Offtime " + str(offTime) + " seconds \n"
    print "Please choose the item you want to start:"
    print "1. Off Zeit definieren"
    print "2. On Zeit definieren"
    print "3. Einamlig"
    print "4. n-Wiederholungen"
    print ""
    print "5. Relais schliessen"
    print "6. Relais öffnen"
    print "\n0. Quit"
    choice = raw_input(" >>  ")
    exec_menu(choice)
 
    return
 
# Execute menu
def exec_menu(choice):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print "Invalid selection, please try again.\n"
            menu_actions['main_menu']()
    return
 

def setOnTime():
    print "OnTime eingeben: "
    choice = raw_input(" >>  ")
    # print "Wert gelesen: " + str(choice)
    global onTime
    onTime = int(choice)
    main_menu()
    return 

def setOffTime():
    print "OffTime eingeben: "
    choice = raw_input(" >>  ")
    global offTime
    offTime = int (choice)
    main_menu()
    return

# Menu 1
def menu1():
    print "Hello Menu 1 !\n"
    print "9. Back"
    print "0. Quit"
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return
 
 
# Back to main menu
def back():
    menu_actions['main_menu']()
 

def oneloop():
    print "do oneloop"
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(relaisGPIO, GPIO.OUT)
    GPIO.output(relaisGPIO, GPIO.LOW)
    time.sleep(onTime)
    GPIO.output(relaisGPIO, GPIO.HIGH)
    time.sleep(offTime)
    return

def nloop():
    print "do n-loops"
    gpioloop()
    return

def closeRelais():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(relaisGPIO, GPIO.OUT)
    GPIO.output(relaisGPIO, GPIO.LOW)
    print "Relais geschlossen Timestamp: " + time.strftime("%d.%m.%Y %H:%M:%S")
    main_menu()
    return

def openRelais():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(relaisGPIO, GPIO.OUT)
    GPIO.output(relaisGPIO, GPIO.HIGH)
    print "Relais geöffnet Timestamp: " + time.strftime("%d.%m.%Y %H:%M:%S")
    main_menu()
    return

def gpioloop():
    # RPi.GPIO Layout verwenden (wie Pin-Nummern)
    GPIO.setmode(GPIO.BOARD)
    
    # Pin 11 (GPIO 17) auf Output setzen
    GPIO.setup(relaisGPIO, GPIO.OUT)
    
    # Dauersschleife
    while 1:
      GPIO.output(relaisGPIO, GPIO.LOW)
      global counter
      counter=counter+1
      print "Relais eingeschalten " + str(counter) + ".loop Timestamp: " + time.strftime("%d.%m.%Y %H:%M:%S")
      time.sleep(offTime)
      GPIO.output(relaisGPIO, GPIO.HIGH)
      time.sleep(onTime)


# Exit program
def exit():
    sys.exit()
 
# =======================
#    MENUS DEFINITIONS
# =======================
 
# Menu definition
menu_actions = {
    'main_menu': main_menu,
    '1': setOffTime,
    '2': setOnTime,
    '3': oneloop,
    '4': nloop,
    '5': closeRelais,
    '6': openRelais, 
    '0': exit,
}
 
# =======================
#      MAIN PROGRAM
# =======================
 
# Main Program
if __name__ == "__main__":
    # Launch main menu
    main_menu()