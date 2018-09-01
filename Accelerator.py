class Accelerator:

    def __init__(self):
        self.speed = 0
        self.targetSpeed = 0
        self.initialized = False
        self.atTargetSpeed = False

    def initialize(self, speed, targetSpeed):
        print("initializing accelerator")
        print(speed)
        print(targetSpeed)
        self.speed = speed
        self.targetSpeed = targetSpeed
        self.initialized = True
        self.atTargetSpeed = False

    def accelerate(self):
        if(self.speed < self.targetSpeed):
            self.speed = self.speed * 1.05
            if(self.speed > self.targetSpeed):
                self.speed = self.targetSpeed
        else:
            self.atTargetSpeed = True

    def reset(self):
        self.speed = 0
        self.initialized = False
        
class Decelerator:

    def __init__(self):
        self.speed = 0
        self.initialized = False
        self.stopped = False
        self.stopSpeed = 0.02

    def initialize(self, speed):
        print("initializing decelerator")
        print(speed)
        self.speed = speed
        self.initialized = True
        self.stopped = False

    def decelerate(self):
        if(self.speed > self.stopSpeed):
            self.speed = self.speed * 0.75
            if(self.speed < self.stopSpeed):
                self.speed = 0
                self.stopped = True
        else:
            self.stopped = True
            self.speed = 0

    def reset(self):
        self.initialized = False