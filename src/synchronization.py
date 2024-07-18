import numpy as np
from scipy.signal import resample
def synchronize_signals(ecg_signal, ppg_signal, sampling_frequency_ecg, sampling_frequency_ppg):
    """
    Synchronize ECG and PPG signals.

    Parameters:
    ecg_signal (array-like): The ECG signal data.
    ppg_signal (array-like): The PPG signal data.
    sampling_frequency_ecg (int or float): The sampling frequency of the ECG signal in Hz.
    sampling_frequency_ppg (int or float): The sampling frequency of the PPG signal in Hz.

    Returns:
    resampled_ecg_signal (numpy array): The resampled ECG signal synchronized with the PPG signal.
    ppg_signal (numpy array): The original PPG signal.
    desired_sampling_frequency (int or float): The sampling frequency used for resampling.
    """

    # Step 1: Calculate the time vector for the PPG signal
    ppg_time = np.arange(len(ppg_signal)) / sampling_frequency_ppg

    # Step 2: Determine the start and end times for the PPG signal
    start_time_ppg = ppg_time[0]
    end_time_ppg = ppg_time[-1]

    # Step 3: Convert these times to corresponding indices in the ECG signal
    start_index_ecg = int(start_time_ppg * sampling_frequency_ecg)
    end_index_ecg = int(end_time_ppg * sampling_frequency_ecg)

    # Step 4: Trim the ECG signal
    trimmed_ecg_signal = ecg_signal[start_index_ecg:end_index_ecg+1]

    # Step 5: Resample signals to have the same sampling frequency
    desired_sampling_frequency = sampling_frequency_ppg  # or any other desired frequency

    # Resample ECG to match the PPG sampling frequency
    number_of_samples_ecg = int(len(trimmed_ecg_signal) * desired_sampling_frequency / sampling_frequency_ecg)
    resampled_ecg_signal = resample(trimmed_ecg_signal, number_of_samples_ecg)

    return resampled_ecg_signal, ppg_signal, desired_sampling_frequency
