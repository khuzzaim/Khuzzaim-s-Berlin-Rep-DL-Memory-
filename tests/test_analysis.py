from spacemed.analysis import find_peaks, calc_heart_rate


def test_find_peaks_simple():
    time = [0, 1, 2, 3, 4]
    signal = [0, 1, 0, 1, 0]

    peaks = find_peaks(time, signal)

    assert list(peaks) == [1, 3]


def test_peak_spacing():
    time = [0, 0.4, 0.8, 1.2, 1.6, 2.0]
    signal = [0, 1, 0.9, 1, 0, 1]

    peaks = find_peaks(time, signal)

    # peaks should not be too close (<0.5 apart)
    for i in range(len(peaks) - 1):
        assert peaks[i + 1] - peaks[i] > 0.5


def test_heart_rate_values():
    time = [0, 1, 2, 3, 4]
    peaks = [1, 3]

    hr = calc_heart_rate(time, peaks)

    assert len(hr) == 1
    assert abs(hr[0] - 30) < 1e-6
