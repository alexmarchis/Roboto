class MotorControllerMock:
    def forward(self, speed):
        print("Going forward with speed: " + str(speed))

    def backward(self, speed):
        print("Going backward with speed: " + str(speed))

    def left(self):
        print("Turning left")

    def right(self):
        print("Turning right")

    def stop(self):
        print("Stopped")