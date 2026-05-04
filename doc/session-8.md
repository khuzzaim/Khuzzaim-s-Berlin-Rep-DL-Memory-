# %%
def compute_slice_activation(data, signal_input, z):
    activation_map = np.zeros(data.shape[:2])
    
    for x in range(data.shape[0]):
        for y in range(data.shape[1]):
            voxel_signal = normalize(data[x, y, z])
            signal_input_n = normalize(signal_input)
            
            cross = sg.correlate(voxel_signal, signal_input_n, mode="same")
            activation_map[x, y] = np.max(cross)
    
    return activation_map