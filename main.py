from majorityVoter import majority_voter
from formalizedPluralityVoter import plurality_voter
from generalizedMedianVoter import generalized_median_voter
from weightedAverageVoter import weighted_average_voter
from mysignal import generate_sinusoidal_signal, add_noise
import matplotlib.pyplot as plt

# Parametry sygnału
frequency = 2  # Hz
amplitude = 1  # Amplituda
duration = 1   # Czas trwania w sekundach
sampling_rate = 500  # Częstotliwość próbkowania w Hz

# Generowanie sygnału sinusoidalnego
t, signal = generate_sinusoidal_signal(frequency, amplitude, duration, sampling_rate)

# Podział sygnału na trzy części i dodanie szumu
noise_level1 = 0.3
noise_level2 = 0.1
noise_level3 = 0.35

signal1 = add_noise(signal, noise_level1)
signal2 = add_noise(signal, noise_level2)
signal3 = add_noise(signal, noise_level3)

# Przepuszczenie sygnałów przez algorytmy głosujące punkt po punkcie
threshold = 0.05
scale = 0.5
output_majority = []
output_plurality = []
output_median = []
output_weighted = []

for i in range(len(signal)):
    votes = [signal1[i], signal2[i], signal3[i]]
    result = majority_voter(votes, threshold)
    output_majority.append(result)

for i in range(len(signal)):
    votes = [signal1[i], signal2[i], signal3[i]]
    result = plurality_voter(votes, threshold)
    output_plurality.append(result)

for i in range(len(signal)):
    votes = [signal1[i], signal2[i], signal3[i]]
    result = generalized_median_voter(votes)
    output_median.append(result)

for i in range(len(signal)):
    votes = [signal1[i], signal2[i], signal3[i]]
    result = weighted_average_voter(votes, scale)
    output_weighted.append(result)

# Wyświetlenie sygnałów
plt.figure(figsize=(12, 10))

plt.subplot(4, 2, 1)
plt.plot(t, signal, label="Oryginalny sygnał")
plt.legend(loc="upper left")

plt.subplot(4, 2, 3)
plt.plot(t, signal1, label="Sygnał z szumem 1")
plt.legend(loc="upper left")

plt.subplot(4, 2, 5)
plt.plot(t, signal2, label="Sygnał z szumem 2")
plt.legend(loc="upper left")

plt.subplot(4, 2, 7)
plt.plot(t, signal3, label="Sygnał z szumem 3")
plt.legend(loc="upper left")

plt.subplot(4, 2, 2)
plt.plot(t, output_majority, label="Sygnał po głosowaniu większościowym")
plt.legend(loc="upper left")

plt.subplot(4, 2, 4)
plt.plot(t, output_plurality, label="Sygnał po głosowaniu licznościowym")
plt.legend(loc="upper left")

plt.subplot(4, 2, 6)
plt.plot(t, output_median, label="Sygnał po głosowaniu medianą")
plt.legend(loc="upper left")

plt.subplot(4, 2, 8)
plt.plot(t, output_weighted, label="Sygnał po głosowaniu wagowym")
plt.legend(loc="upper left")

plt.tight_layout()
plt.show()