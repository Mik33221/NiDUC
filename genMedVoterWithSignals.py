import numpy as np
import matplotlib.pyplot as plt

def compute_distance_matrix(outputs):
    """
    Compute the distance matrix for a given set of outputs.

    Parameters:
    - outputs: List of outputs

    Returns:
    - dist_matrix: 2D list representing the distance matrix
    """
    num_outputs = len(outputs)
    dist_matrix = [[0] * num_outputs for _ in range(num_outputs)]
    for i in range(num_outputs):
        for j in range(i + 1, num_outputs):
            dist_matrix[i][j] = abs(outputs[i] - outputs[j])
            dist_matrix[j][i] = dist_matrix[i][j]  # Distance matrix is symmetric
    return dist_matrix

def generalized_median_voter(outputs):
    """
    Generalized median voter algorithm to select the median output from a set of outputs.

    Parameters:
    - outputs: List of outputs

    Returns:
    - median_output: The median output
    """
    while len(outputs) > 1:
        dist_matrix = compute_distance_matrix(outputs)
        max_distance = max(max(row) for row in dist_matrix)
        max_indices = [(i, j) for i, row in enumerate(dist_matrix) for j, val in enumerate(row) if val == max_distance]
        x_idx, y_idx = max_indices[0]
        x, y = outputs[x_idx], outputs[y_idx]

        current_median = sum(outputs) / len(outputs)
        if abs(x - current_median) < abs(y - current_median):
            outputs.remove(y)
        else:
            outputs.remove(x)
    return outputs[0]

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
noise_level1 = 0.1
noise_level2 = 0.2
noise_level3 = 0.3

signal1 = add_noise(signal, noise_level1)
signal2 = add_noise(signal, noise_level2)
signal3 = add_noise(signal, noise_level3)

# Przepuszczenie sygnałów przez algorytm głosujący punkt po punkcie
output_signal = []

for i in range(len(signal)):
    votes = [signal1[i], signal2[i], signal3[i]]
    result = generalized_median_voter(votes)
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