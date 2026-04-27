def read_pulse(frame):
    datafile = open(frame)
    time = []
    absorption = []
    datafile.readline()
    for line in datafile.readlines():
        line = line.split(",")
        time.append(float(line[0]))
        absorption.append(float(line[1]))
    return time, absorption
