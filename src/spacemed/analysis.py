import numpy as np


def find_peaks(time, absorption):
    """
    Detect peaks in a pulse signal using local maxima and thresholding.

    Parameters:
        time (array-like): Time values of the signal
        absorption (array-like): Signal values

    Returns:
        np.ndarray: Array of detected peak times
    """
    time = np.array(time)
    absorption = np.array(absorption)

    if len(absorption) < 3:
        return np.array([])

    # use threshold
    threshold = np.percentile(absorption, 75)

    peak_indices = (
        np.where(
            (absorption[1:-1] > absorption[:-2])
            & (absorption[1:-1] > absorption[2:])
            & (absorption[1:-1] >= threshold)
        )[0]
        + 1
    )

    peaks = time[peak_indices]

    if len(peaks) == 0:
        return peaks

    # enforce minimum spacing
    filtered = [peaks[0]]
    for t in peaks[1:]:
        if t - filtered[-1] > 0.5:  # increase spacing
            filtered.append(t)

    return np.array(filtered)


def calc_heart_rate(time, peaks):
    """
    Calculate heart rate in beats per minute (BPM) from peak times.

    Parameters:
        time (array-like): Time values
        peaks (array-like): Detected peak times

    Returns:
        np.ndarray: Heart rate values in BPM
    """
    """Calculates heart rate in BPM based on time between peaks."""
    peaks = np.array(peaks)

    if len(peaks) < 2:
        return np.array([])

    delta_t = np.diff(peaks)
    heart_rate = 60 / delta_t
    return heart_rate
