# import packages needed
import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

# declaration of variables
delay = 0.1
button = Button.left
toggle_key = KeyCode(char='a')
stop_key = KeyCode(char='b')

# extends the threading.Thread
# inherit the importa
class ClickMouse(threading.Thread):

    # get the button and delay value
    def __init__(self, delay, button):
        """Initialize variables"""
        # inherit
        super(ClickMouse, self).__init__()

        # get the the button and delay time
        self.delay = delay
        self.button = button

        # declare a new variable
        self.running = False
        self.program_running = True

    def start_clicking(self):
        """start"""
        self.running = True

    def stop_clicking(self):
        """stop"""
        self.running = False

    def exit(self):
        """This will terminate the whole program"""
        self.stop_clicking()
        self.program_running = False

    def run(self):
        """Main loop"""
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.0001)

# creating the instance of the Controller class and recently made class
mouse = Controller()
click_thread = ClickMouse(delay, button)

# starts the loop
click_thread.start()

def on_presss(key):
    """start and stop the program"""
    if key == toggle_key:
        # toggle key, if thread.running is true, it will stop and vice versa
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()

    elif key == stop_key:
        # terminate the whole program
        click_thread.exit()
        listener.stop()

with Listener(on_press=on_presss) as listener:
    listener.join()
