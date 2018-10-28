import os
import pprint
import pygame
import MotorController
#import MotorControllerMock

class ControllerBot(object):

    controller = None
    axis_data = None
    button_data = None
    hat_data = None

    def init(self):
        """Initialize the joystick components"""
        
        pygame.init()
        pygame.joystick.init()
        self.controller = pygame.joystick.Joystick(0)
        self.controller.init()

    def listen(self):
        """Listen for events to happen"""
        
        if not self.axis_data:
            self.axis_data = {}

        if not self.button_data:
            self.button_data = {}
            for i in range(self.controller.get_numbuttons()):
                self.button_data[i] = False

        if not self.hat_data:
            self.hat_data = {}
            for i in range(self.controller.get_numhats()):
                self.hat_data[i] = (0, 0)

        moving = False
        fwSpeed = 0.7
        bwSpeed = 0.5
        turnSpeed = 0.5
        motorController = MotorController.MotorController()
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.JOYAXISMOTION:
                    self.axis_data[event.axis] = round(event.value,2)
                elif event.type == pygame.JOYBUTTONDOWN:
                    self.button_data[event.button] = True
                elif event.type == pygame.JOYBUTTONUP:
                    self.button_data[event.button] = False
                elif event.type == pygame.JOYHATMOTION:
                    self.hat_data[event.hat] = event.value

                # Insert your code on what you would like to happen for each event here!
                # In the current setup, I have the state simply printing out to the screen.
                
               #axis_data
                #0: left right axis of left joystick (left = -1 right = 1)
                #2: left trigger (-1 default, 1 fully pressed)
                #5: right trigger (same as above)
            
                
                if 5 in self.axis_data and self.axis_data[5] > -0.9:
                    forwardSpeed = self.normalizeTrigger(self.axis_data[5], fwSpeed)
                    if(moving == False):
                        moving = True
                        motorController.forward(forwardSpeed)
                    else:
                        motorController.setSpeed(forwardSpeed)
                elif 2 in self.axis_data and self.axis_data[2] > -0.9:
                    backwardSpeed = self.normalizeTrigger(self.axis_data[2], bwSpeed)
                    if(moving == False):
                        moving = True
                        motorController.backward(backwardSpeed)
                    else:
                        motorController.setSpeed(backwardSpeed)
                                                
                elif 0 in self.axis_data and (self.axis_data[0] < -0.1 or self.axis_data[0] > 0.1):
                    speed = self.axis_data[0]
                    if speed < 0:
                        speed = speed * -1
                        speed = self.normalize(speed, turnSpeed)
                        if(moving == False):
                            moving = True
                            motorController.left(speed)
                        else:
                            motorController.setSpeed(speed)
                    elif speed > 0:
                        speed = self.normalize(speed, turnSpeed)
                        if(moving == False):
                            moving = True
                            motorController.right(speed)
                        else:
                            motorController.setSpeed(speed)
                        
                elif moving == True:
                    moving = False
                    motorController.stop()
                        
                    
                
            
    def normalizeTrigger(self, value, maxSpeed):
        value = value + 1
        return self.normalize(value, maxSpeed/2)
    
    def normalize(self, value, maxSpeed):
        return maxSpeed * value

if __name__ == "__main__":
    bot = ControllerBot()
    bot.init()
    bot.listen()