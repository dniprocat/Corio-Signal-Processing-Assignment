from scipy.signal import butter, filtfilt
import numpy as np


def remove_dc_offset(signal):
    """
    Remove DC offset from the signal.

    Parameters:
        signal (np.array): The input signal from which the DC offset will be removed.

    Returns:
        np.array: The signal with the DC offset removed.
    """
    return signal - np.mean(signal)


def lowpass_filter(signal, cutoff, fs, order=5):
    """
    Apply a lowpass filter to the signal.

    Parameters:
        signal (np.array): The input signal to be filtered.
        cutoff (float): The cutoff frequency for the lowpass filter.
        fs (float): The sampling frequency of the signal.
        order (int): The order of the Butterworth filter. Default is 5.

    Returns:
        np.array: The filtered signal.
    """
    nyquist = 0.5 * fs
    norm_cutoff = cutoff / nyquist
    b, a = butter(order, norm_cutoff, btype="low")
    filtered_signal = filtfilt(b, a, signal)
    return filtered_signal


def remove_trend_differencing(signal):
    """
    Remove the trend from the signal using differencing.

    Parameters:
        signal (np.array): The input signal from which the trend will be removed.

    Returns:
        np.array: The detrended signal.
    """
    detrended_signal = np.diff(signal, prepend=signal[0])
    return detrended_signal


def preprocess_signal(signal, fs, cutoff):
    """
    Preprocess the signal by removing DC offset, applying a lowpass filter, and removing trend.

    Parameters:
        signal (np.array): The raw input signal to be preprocessed.
        fs (float): The sampling frequency of the signal.
        cutoff (float): The cutoff frequency for the lowpass filter.

    Returns:
        np.array: The preprocessed signal.
    """
    # Step 1: Remove DC Offset
    signal_no_dc = remove_dc_offset(signal)

    # Step 2: Apply Lowpass Filter
    filtered_signal = lowpass_filter(signal_no_dc, cutoff, fs)

    # Step 3: Remove Trend
    preprocessed_signal = remove_trend_differencing(filtered_signal)

    return preprocessed_signal
