import time

class Train:
    def __init__(self, name, position, speed, max_speed, acceleration):
        self.name = name
        self.position = position
        self.speed = speed
        self.max_speed = max_speed
        self.acceleration = acceleration

    def move(self, other_trains):
        next_position = (self.position + self.speed) % track_length
        for train in other_trains:
            if next_position < self.position:
                if train is not self and train.position > self.position or train.position <= next_position:
                    print(f"Train {self.name} will crash into Train {train.name} if it moves! Stopping...")
                    self.speed = 0
                    return
            else:
                if train is not self and train.position <= next_position and train.position >= self.position:
                    print(f"Train {self.name} will crash into Train {train.name} if it moves! Stopping...")
                    self.speed = 0
                    return
        if self.speed < self.max_speed:
            self.accelerate(self.acceleration)
            
        self.position = next_position

    def accelerate(self, acceleration):
        if self.speed + acceleration <= self.max_speed:
            self.speed += acceleration
        else:
            self.speed = self.max_speed

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
            track_visual[train.position] = train.name
        print(''.join(track_visual))

    def simulate(self, duration):
        for _ in range(duration):
            for train in self.trains:
                train.move(self.trains)
            self.draw_track()
            time.sleep(0.1)  # Delay for better visualization

# Creating trains and track
track_length = 30
track = Track(track_length)

train1 = Train("A", position=1, speed=1, max_speed=2, acceleration=1)
train2 = Train("B", position=track_length // 2, speed=1, max_speed=3, acceleration=3)

# Add trains to the track
track.add_train(train1)
track.add_train(train2)

# Simulate for 20 steps
track.simulate(100)
