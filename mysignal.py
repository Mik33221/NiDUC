import numpy as np

def generate_sinusoidal_signal(frequency, amplitude, duration, sampling_rate):
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    signal = amplitude * np.sin(2 * np.pi * frequency * t)
    return t, signal

def add_noise(signal, noise_level):
    noise = noise_level * np.random.normal(size=signal.shape)
    noisy_signal = signal + noise
    return noisy_signal