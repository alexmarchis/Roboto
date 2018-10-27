from pynput import keyboard
import threading, queue
import MotorController
#import MotorControllerMock

UP_PRESS = "UP_PRESS"
DOWN_PRESS = "DOWN_PRESS"
LEFT_PRESS = "LEFT_PRESS"
RIGHT_PRESS = "RIGHT_PRESS"
RELEASE = "RELEASE"
EXIT = "EXIT"

q = queue.Queue()

def on_press(key):  
    if key == keyboard.Key.up:
       q.put(UP_PRESS)

    if key == keyboard.Key.down:
        q.put(DOWN_PRESS)
    
    if key == keyboard.Key.left:
        q.put(LEFT_PRESS)

    if key == keyboard.Key.right:
        q.put(RIGHT_PRESS)


def on_release(key):
    q.put(RELEASE)
    
    if key == keyboard.Key.esc:
        # Stop listener
        q.put(EXIT)
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:

    motorController = MotorController.MotorController()

    fwSpeed = 0.7
    bwSpeed = 0.5
    turnSpeed = 0.5

    up = False
    down = False
    left = False
    right = False

    while True:
        keyevent = q.get()

        if keyevent == UP_PRESS and up == False:
            up = True
            motorController.forward(fwSpeed)

        if keyevent == DOWN_PRESS and down == False:
            down = True
            motorController.backward(bwSpeed)
        
        if keyevent == LEFT_PRESS and left == False:
            left = True
            motorController.left(turnSpeed)

        if keyevent == RIGHT_PRESS and right == False:
            right = True
            motorController.right(turnSpeed)

        if keyevent == RELEASE:
            up = down = left = right = False
            motorController.stop()
    
        if keyevent == EXIT:
            motorController.stop()
            listener.stop()
            break


