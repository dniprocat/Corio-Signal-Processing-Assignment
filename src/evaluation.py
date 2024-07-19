import numpy as np
from scipy.signal import savgol_filter


def calculate_snr(signal, noise_signal):
    """
    Calculate the Signal-to-Noise Ratio (SNR) of a signal.

    Parameters:
        signal (np.array): The PPG signal data.
        noise_signal (np.array): The noise data extracted from the PPG signal.

    Returns:
        snr (float): The SNR value in dB.
    """
    signal_power = np.mean(signal**2)
    noise_power = np.mean(noise_signal**2)
    snr = 10 * np.log10(signal_power / noise_power)
    return snr


def extract_noise(signal):
    """
    Extract noise from the signal using a specified method.

    Parameters:
        signal (array-like): The PPG signal data.

    Returns:
        noise_signal (np.array): The extracted noise signal.
    """
    smoothed_signal = savgol_filter(signal, window_length=51, polyorder=3)
    noise_signal = signal - smoothed_signal
    return noise_signal
