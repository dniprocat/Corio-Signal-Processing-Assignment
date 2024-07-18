import numpy as np
from scipy.signal import find_peaks, stft


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
    peaks, _ = find_peaks(signal, distance=distance)
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
    pulses, _ = find_peaks(signal, distance=distance)
    return pulses


def detect_outliers_stft(signal, fs, perc_threshold=75, nperseg=256):
    f, t, Zxx = stft(x=signal, fs=fs, nperseg=nperseg)
    magnitude = np.abs(Zxx)
    threshold = np.percentile(magnitude, perc_threshold)
    outliers = np.where(magnitude > threshold)[0]
    return outliers