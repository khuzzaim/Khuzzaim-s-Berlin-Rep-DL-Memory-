import numpy as np

def find_peaks(time, absorption):
    """Identifies local maxima in the signal with a minimum time separation."""
    # Peak detection logic from your script
    peak_indices = np.where(
        (absorption[1:-1] > absorption[:-2]) &
        (absorption[1:-1] > absorption[2:])
    )[0] + 1
    
    peaks = time[peak_indices]
    
    if len(peaks) == 0:
        return np.array([])

    # Filter peaks by 0.3s separation
    filtered_peaks = [peaks[0]]
    for t in peaks[1:]:
        if t - filtered_peaks[-1] > 0.3:
            filtered_peaks.append(t)
            
    return np.array(filtered_peaks)

def calc_heart_rate(peaks):
    """Calculates heart rate in BPM based on time between peaks."""
    delta_t = np.diff(peaks)
    heart_rate = 60 / delta_t
    return heart_rate
