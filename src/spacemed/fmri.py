import numpy as np
from scipy import signal as sg


def normalize(x):
    """Normalize signal using z-score scaling."""

    std = np.std(x)

    if std == 0:
        return np.zeros_like(x)

    return (x - np.mean(x)) / std


def compute_slice_activation(data, signal_input, z):
    """
    Compute activation map for a transverse slice.

    Each voxel is normalized and cross-correlated
    against the stimulus signal.
    """

    activation_map = np.zeros(data.shape[:2])

    signal_input_n = normalize(signal_input)

    for x in range(data.shape[0]):
        for y in range(data.shape[1]):

            voxel_signal = data[x, y, z]

            if np.std(voxel_signal) == 0:
                continue

            voxel_signal_n = normalize(voxel_signal)

            cross = sg.correlate(
                voxel_signal_n,
                signal_input_n,
                mode="same"
            )

            activation_map[x, y] = np.max(cross)

    return activation_map
    return activation_map
