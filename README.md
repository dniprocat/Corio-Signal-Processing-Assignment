# Corio Signal Processing Assignment

This repository contains the solution for the Corio Signal Processing Assignment.

## Project Description

This project involves the following tasks:
1. Identifying the sampling frequencies of the given PPG and ECG signals.
2. Preprocessing the signals to remove high-frequency noise, offset, and trend.
3. Detecting pulse locations in both signals using a simple peak detection method.
4. Detecting anomalies or outliers in the PPG signals.
5. Synchronizing the PPG and ECG signals.
6. Ordering the PPG signals from best to worst according to a chosen evaluation function.

## Solution Techniques Description
1. Identifying Sampling Frequencies
To identify the sampling frequencies of the PPG and ECG signals, we analyzed the signal data and determined the intervals between successive peaks (R-peaks for ECG and Systolic peaks for PPG). This was implemented in the initial steps of the Jupyter notebook.

2. Preprocessing the Signals
The preprocessing step involved removing high-frequency noise using a low-pass filter, removing the offset by subtracting the mean, and detrending the signals to remove linear trends. These steps are implemented in src/preprocessing.py.

3. Pulse Detection
Pulse locations were detected using a simple peak detection algorithm. We utilized the find_peaks function from the SciPy library, which identifies local maxima in the signals. This method is demonstrated in the notebook and implemented in src/analysis.py.

4. Anomaly Detection
We used Short-Time Fourier Transform (STFT) to examine the frequency components over time and applied thresholds based on the 75th percentile to identify significant deviations. This approach is implemented in `src/analysis.py`. Additionally, we used visual analysis to detect anomalous regions.


5. Signal Synchronization
The PPG and ECG signals were synchronized by aligning the detected peaks (pulses) in both signals. We identified the offset between the two signals and shifted one of them to match the other. This synchronization process is detailed in src/synchronization.py.

6. Signal Evaluation
The PPG signals were evaluated based on signal quality metrics such as signal-to-noise ratio (SNR). The signals were then ordered from best to worst according to the chosen evaluation function. This process is described in the notebook and implemented in src/evaluation.py

## Repository Structure

.
├── ECG-PPG processing.ipynb
├── src
│   ├── preprocessing.py
│   ├── evaluation.py
│   ├── analysis.py
│   └── synchronization.py
├── data
│   └── *.npy (PPG/ECG signal files)
├── README.md
└── requirements.txt

## Results

The results of the analysis, including preprocessing, pulse detection, anomaly detection, synchronization, and signal evaluation, are documented and visualized in the Jupyter Notebook `ECG-PPG processing.ipynb`.

