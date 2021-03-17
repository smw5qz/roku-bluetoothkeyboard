#V:1.0
#3-16-21
#SMW
#Roku controller via bluetooth keyboard, running on Pi Zero W microcomputer

#import modules
import time

from roku import Roku as R
tv=R('192.168.1.3')

import keyboard as K

#callback functions for the key listener functions
#button mode, text-entry mode

def thook(event):
    if event.name not in ['backspace','space', 'shift']:
        tv.literal(event.name)
    elif event.name == 'backspace':
        tv.backspace()
    elif event.name == 'space':    
        tv.literal(' ')
def bhook(event):
    
    #physical buttons    
    if event.name == 'h':
        tv.home()
    if event.name == 'left':
        tv.left()
    if event.name == 'right':
        tv.right()
    if event.name == 'up':
        tv.up()
    if event.name == 'down':
        tv.down()
    if event.name == 'enter':
        tv.select()
    if event.name == 'b':
        tv.back()
    if event.name == 'f14':
        tv.volume_down()
    if event.name == 'help':
        tv.volume_up()
    if event.name == 'f13':
        tv.volume_mute()
    if event.name == 'p':
        tv.play()
    #if event.name == 'ff':
        #tv.forward()
    #if event.name == 'rr':
        #tv.reverse()
    #MACROS

    #current show macro
    if event.name == 'c':
        tv['Prime Video'].launch()
        time.sleep(5)
        tv.select()
        time.sleep(3)
        tv.down()
        tv.down()
        tv.select()
        time.sleep(1)
        tv.select()
        time.sleep(3)
        tv.play()

#button and text modes, initiates listening for keypress
#shift button switches between modes indefinitely
#keys unhooked between modes

def bmode(): 
    K.on_press(bhook)
    K.wait('shift')
    K.unhook_all()
    print('entering text mode')
    tmode()

def tmode():
    K.on_press(thook)
    K.wait('shift')
    K.unhook_all()
    print('re-entering button mode')
    bmode()

#begin in button mode
bmode()
