import numpy as np
import matplotlib.pyplot as plt
from random import randint

def distance(vote1, vote2):
    """
    Function to calculate the distance between two votes.

    Parameters:
    - vote1: An integer candidate 1.
    - vote2: An integer candidate 2.

    Returns:
    - The distance between the two votes.
    """
    return abs(vote1 - vote2)

def calculate_weights(votes, a):
    """
    Function to calculate the weights for each vote based on the distance between votes.

    Parameters:
    - votes: A list of integers representing each candidate.
    - a: a fixed constant for scaling

    Returns:
    - A list of weights for each vote.
    - The sum of the weights for normalisation.
    """
    weights = []

    for i, vote in enumerate(votes):
        product = 1
        for j, other_vote in enumerate(votes):
            if i != j:
                product *= distance(vote, other_vote)/(a**2)
        weight = (1 + product)**-1
        weights.append(weight)

    return weights, sum(weights)

def weighted_average_voter(votes, scale):
    """
    Function to determine the winner based on a weighted average vote. Weights are calculated based on the distance between votes, in such a way
    that large numbers won't have a big impact on the result.

    Parameters:
    - votes: A list of integers representing the votes for each candidate.

    Returns:
    - The winning candidate index (1-indexed), or None if there is a tie.
    """
    weights, sum_weights = calculate_weights(votes, scale)
    return sum([vote*(weight/sum_weights) for vote, weight in zip(votes, weights)])


# Funkcje do generowania sygnałów

def generate_sinusoidal_signal(frequency, amplitude, duration, sampling_rate):
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    signal = amplitude * np.sin(2 * np.pi * frequency * t)
    return t, signal

def add_noise(signal, noise_level):
    noise = noise_level * np.random.normal(size=signal.shape)
    noisy_signal = signal + noise
    return noisy_signal

# Parametry sygnału
frequency = 5  # Hz
amplitude = 1  # Amplituda
duration = 2   # Czas trwania w sekundach
sampling_rate = 500  # Częstotliwość próbkowania w Hz

# Generowanie sygnału sinusoidalnego
t, signal = generate_sinusoidal_signal(frequency, amplitude, duration, sampling_rate)

# Podział sygnału na trzy części i dodanie szumu
noise_level1 = 0
noise_level2 = 0.1
noise_level3 = 0.1

signal1 = add_noise(signal, noise_level1)
signal2 = add_noise(signal, noise_level2)
signal3 = add_noise(signal, noise_level3)

# Przepuszczenie sygnałów przez algorytm głosujący punkt po punkcie
threshold = 0.0005
output_signal = []

for i in range(len(signal)):
    votes = [signal1[i], signal2[i], signal3[i]]
    result = weighted_average_voter(votes, threshold)
    if result is None:
        # Jeśli nie ma wyniku, użyj średniej jako wartość domyślną
        result = np.mean(votes)
    output_signal.append(result)

# Wyświetlenie sygnałów
plt.figure(figsize=(12, 10))

plt.subplot(5, 1, 1)
plt.plot(t, signal, label="Oryginalny sygnał")
plt.legend()

plt.subplot(5, 1, 2)
plt.plot(t, signal1, label="Sygnał z szumem 1")
plt.legend()

plt.subplot(5, 1, 3)
plt.plot(t, signal2, label="Sygnał z szumem 2")
plt.legend()

plt.subplot(5, 1, 4)
plt.plot(t, signal3, label="Sygnał z szumem 3")
plt.legend()

plt.subplot(5, 1, 5)
plt.plot(t, output_signal, label="Sygnał po głosowaniu")
plt.legend()

plt.tight_layout()
plt.show()