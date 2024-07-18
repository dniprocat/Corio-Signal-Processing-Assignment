from scipy.signal import butter, filtfilt, detrend
import numpy as np


def remove_dc_offset(signal):
    """
    Remove DC offset from signal.
    Args:
        signal (np.array): Signal

    Returns:
        np.array: Signal with DC offset removed.
    """
    # Just subtract the mean
    return signal - np.mean(signal)


def lowpass_filter(signal, cutoff, fs, order=5):
    """
    Lowpass filter.
    Args:
        signal:
        cutoff:
        fs:
        order:

    Returns:

    """
    nyquist = 0.5 * fs
    norm_cutoff = cutoff / nyquist
    b, a = butter(order, norm_cutoff, btype='low')
    filtered_signal = filtfilt(b, a, signal)
    return filtered_signal


def remove_trend_differencing(signal):
    """
    Remove Trend.
    Args:
        signal:

    Returns:

    """
    detrended_signal = np.diff(signal, prepend=signal[0])
    return detrended_signal


def preprocess_signal(signal, fs, cutoff):
    """
    Final preprocessing of signal.
    Args:
        signal:
        fs:
        cutoff:

    Returns:

    """
    # Step 1: Remove DC Offset
    signal_no_dc = remove_dc_offset(signal)

    # Step 2: Apply Lowpass Filter
    filtered_signal = lowpass_filter(signal_no_dc, cutoff, fs)

    # Step 3: Remove Trend
    preprocessed_signal = remove_trend_differencing(filtered_signal)

    return preprocessed_signal
