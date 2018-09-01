from pynput import keyboard
import threading, queue
#import MotorController
import MotorControllerMock
import Accelerator
import time

UP_PRESS = "UP_PRESS"
DOWN_PRESS = "DOWN_PRESS"
LEFT_PRESS = "LEFT_PRESS"
RIGHT_PRESS = "RIGHT_PRESS"
RELEASE = "RELEASE"
DECELERATE = "DECELERATE"
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

    motorController = MotorControllerMock.MotorControllerMock()

    accelerator = Accelerator.Accelerator()
    decelerator = Accelerator.Decelerator()

    while True:
        if q.empty() and decelerator.initialized:
            keyevent = DECELERATE
        else:
            keyevent = q.get()
            if decelerator.initialized:
                print("reseting decelerator")
                decelerator.reset()

        if keyevent == UP_PRESS:
            if(accelerator.initialized):
                accelerator.accelerate()
                if(accelerator.atTargetSpeed == False):
                    time.sleep(0.01)
                    motorController.setSpeed(accelerator.speed)
            else:
                accelerator.initialize(0.3, 0.8)
                motorController.forward(accelerator.speed)

        if keyevent == DOWN_PRESS:
            if(accelerator.initialized):
                accelerator.accelerate()
                if(accelerator.atTargetSpeed == False):
                    time.sleep(0.05)                    
                    motorController.setSpeed(accelerator.speed)
            else:
                accelerator.initialize(0.2, 0.6)
                motorController.backward(accelerator.speed)
        
        if keyevent == LEFT_PRESS:
            if(accelerator.initialized):
                accelerator.accelerate()
                if(accelerator.atTargetSpeed == False):
                    motorController.setSpeed(accelerator.speed)
            else:
                accelerator.initialize(0.2, 0.5)
                motorController.left(accelerator.speed)

        if keyevent == RIGHT_PRESS:
            if(accelerator.initialized):
                accelerator.accelerate()
                if(accelerator.atTargetSpeed == False):
                    motorController.setSpeed(accelerator.speed)
            else:
                accelerator.initialize(0.2, 0.5)
                motorController.right(accelerator.speed)

        if keyevent == RELEASE:
            speed = accelerator.speed
            accelerator.reset()            
            decelerator.initialize(speed) 

        if keyevent == DECELERATE:
            decelerator.decelerate()
            if(decelerator.stopped == False):
                motorController.setSpeed(decelerator.speed)
                time.sleep(0.05)
            else:
                print("stopped decelerating")
                decelerator.reset()
    
        if keyevent == EXIT:
            listener.stop()
            break


