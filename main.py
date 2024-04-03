import time

class Train:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.position = 0

    def move(self):
        self.position += self.speed

    def accelerate(self, acceleration):
        self.speed += acceleration

    def decelerate(self, deceleration):
        if self.speed - deceleration >= 0:
            self.speed -= deceleration
        else:
            self.speed = 0

class Track:
    def __init__(self, length):
        self.length = length
        self.trains = []

    def add_train(self, train):
        self.trains.append(train)

    def draw_track(self):
        track_visual = ['_' for _ in range(self.length)]
        for train in self.trains:
            if 0 <= train.position < self.length:
                track_visual[train.position] = train.name
        print(''.join(track_visual))

    def simulate(self, duration):
        for _ in range(duration):
            for train in self.trains:
                train.move()
                if train.position >= self.length:
                    print(f"{train.name} has reached the end of the track!")
                    self.trains.remove(train)
            self.draw_track()
            time.sleep(0.1)  # Delay for better visualization

# Creating trains and track
track_length = 20
track = Track(track_length)

train1 = Train("A", speed=2)
train2 = Train("B", speed=3)

# Add trains to the track
track.add_train(train1)
track.add_train(train2)

# Simulate for 50 steps
track.simulate(20)
