import argparse
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

from .load_pulse import read_pulse
from .analysis import find_peaks
from .analysis import calc_heart_rate


def arg_parser():
    parser = argparse.ArgumentParser(description="Plot heart rate from pulse data")

    parser.add_argument("data", type=Path, help="Path to input pulse data CSV file")

    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path("heart_rate.pdf"),
        help="Output PDF file",
    )

    return parser


def main():
    """
    Main function to load pulse data, detect peaks,
    calculate heart rate, and generate a plot.

    Uses command-line arguments for input and output files.
    """
    parser = arg_parser()
    args = parser.parse_args()

    indata = args.data
    outname = args.output

    time, absorption = read_pulse(indata)

    peaks = find_peaks(time, absorption)

    heart_rates = calc_heart_rate(time, peaks)
    hr_mean = heart_rates.mean() if len(heart_rates) > 0 else 0

    time = np.array(time)
    absorption = np.array(absorption)

    indices = [np.argmin(np.abs(time - p)) for p in peaks]
    peak_values = absorption[indices]

    plt.plot(time, absorption, label="Pulse signal")
    plt.scatter(peaks, peak_values, color="red", label="Peaks")

    plt.title(f"Heart Rate: {hr_mean:.2f} bpm")
    plt.xlabel("Time (s)")
    plt.ylabel("Absorption")
    plt.grid(True)
    plt.legend()

    plt.savefig(outname)
    plt.close()


if __name__ == "__main__":
    main()
