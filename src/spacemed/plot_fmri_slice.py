import argparse

import matplotlib.pyplot as plt
import nibabel as nib
import numpy as np
from scipy.ndimage import gaussian_filter

from spacemed.fmri import compute_slice_activation


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("fmri_file")
    parser.add_argument("slice_index", type=int)
    parser.add_argument("output_file")

    args = parser.parse_args()

    fmri = nib.load(args.fmri_file)
    data = fmri.get_fdata()

    nt = data.shape[-1]

    sone = np.array([1] * 5 + [0] * 5)

    signal_input = np.tile(
        sone,
        int(np.ceil(nt / len(sone)))
    )

    signal_input = signal_input[:nt]

    activation_map = compute_slice_activation(
        data,
        signal_input,
        args.slice_index
    )

    # Gaussian filtering suppresses voxel-level noise
    activation_smooth = gaussian_filter(
        activation_map,
        sigma=1
    )

    # Keep strongest activations only.
    # NaN values are not plotted.
    threshold = np.percentile(
        activation_smooth,
        90
    )

    activation_thresh = np.where(
        activation_smooth > threshold,
        activation_smooth,
        np.nan
    )

    plt.imshow(
        data[:, :, args.slice_index, 0].T,
        cmap="gray",
        origin="lower"
    )

    plt.imshow(
        activation_thresh.T,
        cmap="hot",
        origin="lower",
        alpha=0.6
    )

    plt.colorbar()

    plt.title(
        f"Activation Map Overlay Slice {args.slice_index}"
    )

    plt.savefig(args.output_file)


if __name__ == "__main__":
    main()
