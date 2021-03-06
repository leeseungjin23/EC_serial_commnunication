# This file is a part of EC_serial_communication
# BSD 3-Clause License
#
# Copyright (c) 2019, Intelligent-distributed Cloud and Security Laboratory (ICNS Lab.)
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# title           : serial_input.py
# description     : Python, edge cloud serial communication
# author          : Yunhwan Kim.
# date            : 20190822
# version         : 0.3
# notes           : This EC_serial_communication is an implementation of edge cloud for communicating
# 				 self-driving cart and edge cloud.

import threading
import time
import numpy as np
import serial
#import zbar
import sys, getopt
import pygame
import Adafruit_GPIO as GPIO
import Adafruit_CharLCD as LCD


from pynput import keyboard, mouse


lcd_rs = 25
lcd_en = 24
lcd_d4 = 23
lcd_d5 = 17
lcd_d6 = 18
lcd_d7 = 22
lcd_backlight = 2
# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows = 2
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)
ser = serial.Serial(
    "/dev/ttyAMA0",
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    writeTimeout=1,
    timeout=10,
    rtscts=False,
    dsrdtr=False,
    xonxoff=False)


def on_press(key):
    try:
        ser.write('{0}'.format(key).encode())
        lcd.message('{0}'.format(key))
        print('{0}'.format(key))
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
'''
# Initialize the game engine
pygame.init()

# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0) 

# Set the height and width of the screen
size   = [400, 300]
screen = pygame.display.set_mode(size)
#font = pygame.font.SysFont("consolas", 20)
 
#pygame.display.set_caption("Game Title")

#Loop until the user clicks the close button.
done  = False
flag  = None
clock = pygame.time.Clock()


# print text function
def printText(msg, color='BLACK', pos=(50, 50)):
    textSurface      = font.render(msg, True, pygame.Color(color), None)
    textRect         = textSurface.get_rect()
    textRect.topleft = pos
 
    screen.blit(textSurface, textRect)

while not done:
 
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we willimport Adafruit_GPIO as GPIO


    clock.tick(10)
     
    # Main Event Loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.KEYDOWN: # If user release what he pressed.
            pressed = pygame.key.get_pressed()
            buttons = [pygame.key.name(k) for k,v in enumerate(pressed) if v]
            flag = True
        elif event.type == pygame.KEYUP: # If user press any key.
            flag = False
        elif event.type == pygame.QUIT:  # If user clicked close.
            done = True                 
 
     
    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.
      
    # Clear the screen and set the screen background
  #  screen.fill(WHITE)
 
    # Print red text if user pressed any key.
    if flag == True:
 #       printText('you just key down!!', 'RED')
 #       printText('--> you pressed any key.', 'RED', (50, 70))
 #       printText('Pressed Key : ' + buttons[0], 'RED', (50, 90))
        ser.write(buttons[0].encode())
        lcd.message(buttons[0])
        print(buttons[0])
 
    # Print blue text if user released any key.
    elif flag == False:
  #      printText('you just key up!!', 'BLUE')
  #      printText('--> released what you pressed.', 'BLUE', (50, 70))
        print(buttons[0])
    # Print default text if user do nothing.
  #  else:
  #      printText('Please press any key.')
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
#    pygame.display.flip()
 
# Be IDLE friendly
pygame.quit()
'''