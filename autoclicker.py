import time
import threading
from pynput.mouse import Button, Controller as mController
from pynput.keyboard import Listener, KeyCode, Controller as kController

# Modifiable variables, including delay between clicks, button to autoclick, and the start/stop keys
delay = 0.01
start_key = KeyCode(char='a')
stop_key = KeyCode(char='s')
button = Button.left # Switch button to keybind if you want with char

# Class that instantiates all variables, sets running state, and 
class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super().__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    # Method to start clicker run event
    def start_clickcing(self):
        self.running = True
    
    # Method to stop clicker run event
    def stop_clicking(self):
        self.running = False

    # Clicking loop
    def run(self):
        while self.program_running:
            while self.running:
                print('clicked')
                # mouse.click(self.button)
                
                # Uncoment these two for keyboard:
                # keyboard.press(button)
                # keyboard.release(button)

                time.sleep(self.delay)

    # End the program
    def exit(self):
        self.stop_clicking()
        self.program_running = False

# Setting mouse to controller for function application
mouse = mController()
keyboard = kController()
clicker = ClickMouse(delay, button)
clicker.start()

# Detector to check which keys are pressed
def on_press(key):
    # Starts autoclicker
    if key == start_key and not clicker.running:
        print('click start')
        clicker.start_clickcing()
    # Stops autoclicker
    elif key == start_key:
        print('click stop')
        clicker.stop_clicking()
    # Ends program
    elif key == stop_key:
        print('Program ended')
        clicker.exit()
        listener.stop()

# Turning on listener  
with Listener(on_press=on_press) as listener:
    listener.join()
