import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk
from majorityVoter import majority_voter
from formalizedPluralityVoter import plurality_voter
from generalizedMedianVoter import generalized_median_voter
from weightedAverageVoter import weighted_average_voter
from mysignal import *

# GUI application
class SignalSimulator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Signal Simulator")

        self.frequency = 5
        self.amplitude = 1
        self.duration = 2
        self.sampling_rate = 500
        self.noise_level1 = 0.1
        self.noise_level2 = 0.1
        self.noise_level3 = 0.1
        self.threshold = 0.05
        self.scale = 1
        self.voter_algorithm = 'Majority Voter'

        self.init_ui()

    def init_ui(self):
        params_frame = ttk.Frame(self)
        params_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.create_slider(params_frame, "Frequency (Hz)", 0.1, 10.0, self.frequency, self.set_frequency)
        self.create_slider(params_frame, "Amplitude", 0.1, 5.0, self.amplitude, self.set_amplitude)
        self.create_slider(params_frame, "Duration (s)", 0.1, 5.0, self.duration, self.set_duration)
        self.create_slider(params_frame, "Sampling Rate (Hz)", 100, 2000, self.sampling_rate, self.set_sampling_rate)
        self.create_slider(params_frame, "Noise Level 1", 0.0, 1.0, self.noise_level1, self.set_noise_level1)
        self.create_slider(params_frame, "Noise Level 2", 0.0, 1.0, self.noise_level2, self.set_noise_level2)
        self.create_slider(params_frame, "Noise Level 3", 0.0, 1.0, self.noise_level3, self.set_noise_level3)
        self.create_slider(params_frame, "Threshold", 0.01, 0.2, self.threshold, self.set_threshold)
        self.create_slider(params_frame, "Scale", 0.1, 5.0, self.scale, self.set_scale)

        # Dropdown menu for voting algorithm selection
        algo_label = ttk.Label(params_frame, text="Voting Algorithm")
        algo_label.pack(side=tk.TOP, fill=tk.X)
        self.algo_selector = ttk.Combobox(params_frame,
                                          values=['Majority Voter', 'Generalized Median Voter', 'Plurality Voter',
                                                  'Weighted Average Voter'])
        self.algo_selector.set(self.voter_algorithm)
        self.algo_selector.pack(side=tk.TOP, fill=tk.X)
        self.algo_selector.bind("<<ComboboxSelected>>", self.set_voter_algorithm)

        plot_button = ttk.Button(params_frame, text="Plot Signals", command=self.plot_signals)
        plot_button.pack(side=tk.TOP, fill=tk.X)

        figure_frame = ttk.Frame(self)
        figure_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        self.figure = plt.Figure(figsize=(10, 10))
        self.canvas = FigureCanvasTkAgg(self.figure, master=figure_frame)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def create_slider(self, parent, label, min_value, max_value, init_value, callback):
        frame = ttk.Frame(parent)
        frame.pack(side=tk.TOP, fill=tk.X)
        label_widget = ttk.Label(frame, text=f"{label}: {init_value}")
        label_widget.pack(side=tk.LEFT)
        slider = ttk.Scale(frame, from_=min_value, to=max_value, value=init_value, orient=tk.HORIZONTAL,
                           command=lambda value: self.update_slider(label_widget, label, value, callback))
        slider.pack(side=tk.RIGHT, fill=tk.X, expand=True)

    def update_slider(self, label_widget, label, value, callback):
        callback(float(value))
        label_widget.config(text=f"{label}: {float(value):.2f}")

    def set_frequency(self, value):
        self.frequency = value

    def set_amplitude(self, value):
        self.amplitude = value

    def set_duration(self, value):
        self.duration = value

    def set_sampling_rate(self, value):
        self.sampling_rate = value

    def set_noise_level1(self, value):
        self.noise_level1 = value

    def set_noise_level2(self, value):
        self.noise_level2 = value

    def set_noise_level3(self, value):
        self.noise_level3 = value

    def set_threshold(self, value):
        self.threshold = value

    def set_scale(self, value):
        self.scale = value

    def set_voter_algorithm(self, event):
        self.voter_algorithm = self.algo_selector.get()

    def plot_signals(self):
        self.figure.clear()

        frequency = self.frequency
        amplitude = self.amplitude
        duration = self.duration
        sampling_rate = self.sampling_rate
        noise_level1 = self.noise_level1
        noise_level2 = self.noise_level2
        noise_level3 = self.noise_level3
        threshold = self.threshold
        scale = self.scale
        voter_algorithm = self.voter_algorithm

        t, signal = generate_sinusoidal_signal(frequency, amplitude, duration, sampling_rate)
        noisy_signal1 = add_noise(signal, noise_level1)
        noisy_signal2 = add_noise(signal, noise_level2)
        noisy_signal3 = add_noise(signal, noise_level3)

        if voter_algorithm == 'Majority Voter':
            voted_signal = [majority_voter([noisy_signal1[i], noisy_signal2[i], noisy_signal3[i]], threshold) for i in
                            range(len(t))]
        elif voter_algorithm == 'Generalized Median Voter':
            voted_signal = [generalized_median_voter([noisy_signal1[i], noisy_signal2[i], noisy_signal3[i]]) for i in
                            range(len(t))]
        elif voter_algorithm == 'Plurality Voter':
            voted_signal = [plurality_voter([noisy_signal1[i], noisy_signal2[i], noisy_signal3[i]], threshold) for i in
                            range(len(t))]
        elif voter_algorithm == 'Weighted Average Voter':
            voted_signal = [weighted_average_voter([noisy_signal1[i], noisy_signal2[i], noisy_signal3[i]], scale) for i
                            in range(len(t))]

        ax1 = self.figure.add_subplot(511)
        ax1.plot(t, signal, label="Original Signal")
        ax1.legend()

        ax2 = self.figure.add_subplot(512)
        ax2.plot(t, noisy_signal1, label="Noisy Signal 1")
        ax2.legend()

        ax3 = self.figure.add_subplot(513)
        ax3.plot(t, noisy_signal2, label="Noisy Signal 2")
        ax3.legend()

        ax4 = self.figure.add_subplot(514)
        ax4.plot(t, noisy_signal3, label="Noisy Signal 3")
        ax4.legend()

        ax5 = self.figure.add_subplot(515)
        #ax5.plot(t, noisy_signal1, label="Noisy Signal 1", alpha=0.5)
        #ax5.plot(t, noisy_signal2, label="Noisy Signal 2", alpha=0.5)
        #ax5.plot(t, noisy_signal3, label="Noisy Signal 3", alpha=0.5)
        ax5.plot(t, voted_signal, label="Output Signal (Voted)", linewidth=2)
        ax5.legend()

        self.canvas.draw()


if __name__ == "__main__":
    app = SignalSimulator()
    app.mainloop()