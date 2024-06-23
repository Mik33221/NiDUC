import numpy as np
import matplotlib.pyplot as plt
from random import randint

def majority_voter_sets(votes, threshold):
    """
    Function to determine the winner based on a majority vote with a specified threshold.

    Parameters:
    - votes: A list of integers representing values to be voted on.
    - threshold: A float representing the maximum difference of between values to be considered "same"

    Returns:
    - subsets: A list of subsets of votes grouped by the threshold
    """
    subsets = []
    i = 0
    while len(votes) > 0 and i < len(votes):
        subset = [votes[i]]
        j = i + 1
        while j < len(votes):
            if abs(votes[i] - votes[j]) <= threshold:
                subset.append(votes[j])
                votes.pop(j)
            else:
                j += 1
        subsets.append(subset)
        votes.pop(i)
    return subsets

def majority_voter(votes, threshold):
    """
    Function to determine the winner based on a majority vote with a specified threshold.

    Parameters:
    - votes: A list of integers representing values to be voted on.
    - threshold: A float representing the maximum difference of between values to be considered "same"

    Returns:
    - The winning value or None if no majority is found.
    """
    N = len(votes)
    subsets = majority_voter_sets(votes, threshold)
    if not subsets:  # Check if subsets is empty
        return -1

    biggestSet = subsets[0]
    for set in subsets:
        if len(set) > len(biggestSet):
            biggestSet = set

    if len(biggestSet) < (N + 1) / 2:
        return -1

    subsets.remove(biggestSet)

    for set in subsets:
        if len(biggestSet) <= len(set):
            return 0

    return biggestSet[randint(0, len(biggestSet) - 1)]

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
threshold = 0.05
output_signal = []

for i in range(len(signal)):
    votes = [signal1[i], signal2[i], signal3[i]]
    result = majority_voter(votes, threshold)
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