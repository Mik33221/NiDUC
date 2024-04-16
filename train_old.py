import random
import numpy as np
import matplotlib.pyplot as plt

class Train:
    def __init__(self, length, initial_speed=0):
        self.length = length
        self.position = 0
        self.speed = initial_speed
        self.acceleration = 0
        self.max_speed = 30  # Maximum speed in m/s
        self.brake_rate = 2  # Brake rate in m/s^2
        self.acceleration_rate = 1  # Acceleration rate in m/s^2
        self.sensors = [0, 0, 0]  # Three sensors at the front of the train
        self.brake_engaged = False

    def move(self, time_step):
        self.speed += self.acceleration * time_step
        if self.speed < 0:
            self.speed = 0
        elif self.speed > self.max_speed:
            self.speed = self.max_speed
        self.position += self.speed * time_step

    def update_sensors(self, obstacles):
        # Simulate sensor readings based on obstacles
        for i in range(len(self.sensors)):
            # Check if any obstacle is in the sensor's range
            if any(self.position + j * 10 <= obstacles[i] <= self.position + (j+1) * 10 for j in range(self.length)):
                self.sensors[i] = 1  # Obstacle detected
            else:
                self.sensors[i] = 0

    def should_engage_brake(self):
        # Use majority voting system to decide whether to engage brake
        if sum(self.sensors) >= 2:  # If at least two sensors detect obstacle
            return True
        return False

    def engage_brake(self):
        self.acceleration = -self.brake_rate
        self.brake_engaged = True

    def release_brake(self):
        self.acceleration = self.acceleration_rate
        self.brake_engaged = False

    def simulate(self, time_steps, terrain):
        position_history = [self.position]
        speed_history = [self.speed]
        for t in range(1, time_steps + 1):
            self.update_sensors(terrain)
            if self.should_engage_brake():
                self.engage_brake()
            else:
                self.release_brake()
            self.move(1)
            position_history.append(self.position)
            speed_history.append(self.speed)
        return position_history, speed_history

def generate_terrain(length, complexity):
    # Generate random terrain heights
    terrain = [random.randint(0, complexity) for _ in range(length)]
    return terrain

def main():
    train_length = 5  # Length of the train (number of cars)
    time_steps = 100  # Number of time steps to simulate
    terrain_length = time_steps * 10  # Length of terrain
    terrain_complexity = 10  # Complexity of the terrain

    train = Train(train_length)
    terrain = generate_terrain(terrain_length, terrain_complexity)

    position_history, speed_history = train.simulate(time_steps, terrain)

    # Plotting train position and speed
    plt.figure(figsize=(12, 6))
    plt.subplot(2, 1, 1)
    plt.plot(range(len(position_history)), position_history, label='Position')
    plt.xlabel('Time Step')
    plt.ylabel('Position (m)')
    plt.title('Train Position Over Time')
    plt.grid(True)
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(range(len(speed_history)), speed_history, label='Speed')
    plt.xlabel('Time Step')
    plt.ylabel('Speed (m/s)')
    plt.title('Train Speed Over Time')
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
