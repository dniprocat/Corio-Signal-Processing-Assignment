import numpy as np
from scipy.signal import find_peaks
def detect_sampling_freq(signal, bps, distance=None):
    """
    Detect the sampling frequency of a given signal.

    Parameters:
    signal (np.array): The signal array.
    bps (int or float): Pre-known HR in beats per second
    distance (int): Typical distance between the peaks

    Returns:
    sampling_frequency (float): The detected sampling frequency.
    """
    peaks, _ = find_peaks(signal, distance)
    sum_interval = np.sum(np.diff(peaks))
    n = len(peaks)
    frequency = sum_interval / n / bps
    return frequency

def puls_loc(signal, distance=None):
    """
    Detect the location of pulses in a signal.
    Args:
        signal (np.array): The signal array.
        distance (int or float): Most likely pulse distance.
    Returns:
        pulses (np.array): The detected pulses.
    """
    pulses, _ = find_peaks(signal, distance)
    return pulses
