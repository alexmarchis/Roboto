class MotorControllerMock:
    def forward(self, speed):
        print("Going forward with speed: " + str(speed))

    def backward(self, speed):
        print("Going backward with speed: " + str(speed))

    def left(self, speed):
        print("Turning left with speed: " + str(speed))

    def right(self, speed):
        print("Turning right with speed: " + str(speed))

    def setSpeed(self, speed):
        print("Setting speed: " + str(speed))
        

    def stop(self):
        print("Stopped")