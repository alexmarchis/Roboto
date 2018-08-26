from pynput import keyboard
import threading, queue
import MotorController
import MotorControllerMock

UP_PRESS = "UP_PRESS"
DOWN_PRESS = "DOWN_PRESS"
LEFT_PRESS = "LEFT_PRESS"
RIGHT_PRESS = "RIGHT_PRESS"
UP_RELEASE = "UP_RELEASE"
DOWN_RELEASE = "DOWN_RELEASE"
LEFT_RELEASE = "LEFT_RELEASE"
RIGHT_RELEASE = "RIGHT_RELEASE"
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
    if key == keyboard.Key.up:
       q.put(UP_RELEASE)

    if key == keyboard.Key.down:
        q.put(DOWN_RELEASE)
    
    if key == keyboard.Key.left:
        q.put(LEFT_RELEASE)

    if key == keyboard.Key.right:
        q.put(RIGHT_RELEASE)
    
    if key == keyboard.Key.esc:
        # Stop listener
        q.put(EXIT)
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:

    motorController = MotorController.MotorController()

    up = False
    down = False
    left = False
    right = False

    while True:
        keyevent = q.get()
        if keyevent == UP_PRESS and up == False:
            up=True
            motorController.forward(0.3)

        if keyevent == DOWN_PRESS and down == False:
            down=True
            motorController.backward(0.3)
        
        if keyevent == LEFT_PRESS and left == False:
            left=True
            motorController.left()

        if keyevent == RIGHT_PRESS and right == False:
            right=True
            motorController.right()

        if keyevent == UP_RELEASE and up == True:
            up=False
            motorController.stop()

        if keyevent == DOWN_RELEASE and down == True:
            down=False
            motorController.stop()
        
        if keyevent == LEFT_RELEASE and left == True:
            left=False
            motorController.stop()

        if keyevent == RIGHT_RELEASE and right == True:
            right=False
            motorController.stop()

        if keyevent == EXIT:
            listener.stop()
            break


