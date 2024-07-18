import numpy as np
from scipy.signal import savgol_filter

def calculate_snr(signal, noise_signal):
    """
    Calculate the Signal-to-Noise Ratio (SNR) of a signal.

    Parameters:
    signal (array-like): The PPG signal data.
    noise_signal (array-like): The noise data extracted from the PPG signal.

    Returns:
    float: The SNR value in dB.
    """
    signal_power = np.mean(signal**2)
    noise_power = np.mean(noise_signal**2)
    snr = 10 * np.log10(signal_power / noise_power)
    return snr


def extract_noise(signal, method='simple'):
    """
    Extract noise from the signal using a specified method.

    Parameters:
    signal (array-like): The PPG signal data.
    method (str): The method to use for noise extraction. Default is 'simple'.

    Returns:
    array-like: The extracted noise signal.
    """
    if method == 'simple':
        # A simple method to extract noise is to subtract a smoothed version of the signal from the original signal
        smoothed_signal = savgol_filter(signal, window_length=51, polyorder=3)
        noise_signal = signal - smoothed_signal
    else:
        raise ValueError("Unsupported method for noise extraction.")

    return noise_signal
