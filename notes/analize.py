#!/bin/env python
"""TODO Write some nice docstring"""

from argparse import ArgumentParser
from matplotlib import pyplot as plt
import numpy as np

g = 9.80665  # gravity in m/s according to ???
kmph = 3.6  # converts from m/s to km/h

parser = ArgumentParser(description=__doc__)
parser.add_argument("file", help="input filepath (must be a .csv)")
args = parser.parse_args()

data = np.loadtxt(args.file, delimiter=",").T

data[1] -= data[1].min()  # start counting time at zero
data[1] /= 60000  # convert timestamps from milliseconds to minutes

# plt.title("engine rpm over time (min)")
# data[4] /= data[0]
# plt.plot(data[1], data[4])
# plt.show()

# plt.title("engine rpm over time (min)")
# drpm = np.diff(data[4])
# drpm /= data[0][:-1]
# plt.scatter(data[4][:-1], drpm)
# plt.show()

# plt.title("car acceleration (g) over time (min)")
# data[5] /= g*data[0]
# data[6] /= g*data[0]
# data[7] /= g*data[0]
# plt.axhline(y=0, color="black", alpha=0.1)
# plt.plot(data[1], data[7], label="longitudinal (forward positive)")
# plt.plot(data[1], data[5], label="lateral (positive to the right)")
# plt.plot(data[1], data[6], label="vertical (up is positive)")
# plt.legend()
# plt.show()

# plt.title("car valocity (km/h) over time (min)")
# data[8] /= data[0]/kmph
# data[9] /= data[0]/kmph
# data[10] /= data[0]/kmph
# plt.axhline(y=0, color="black", alpha=0.1)
# plt.plot(data[1], data[10], label="longitudinal (forward positive)")
# plt.plot(data[1], data[8], label="lateral (positive to the right)")
# plt.plot(data[1], data[9], label="vertical (up is positive)")
# plt.legend()
# plt.show()

# TODO all
# TODO ser for rad/s converter para graus ou revolutions/s ou rpm
# TODO grafico polar
# plt.title("car rotation speed (rad/s???) over time (min)")
# data[11] /= data[0]
# data[12] /= data[0]
# data[13] /= data[0]
# plt.axhline(y=0, color="black", alpha=0.1)
# plt.plot(data[1], data[11], label="right/pitch")
# plt.plot(data[1], data[12], label="up/yaw")
# plt.plot(data[1], data[13], label="forward/roll")
# plt.legend()
# plt.show()

# TODO grafico polar
# plt.title("car direction (degrees) over time (min)")
# data[14] = np.rad2deg(data[14])/data[0]
# data[15] = np.rad2deg(data[15])/data[0]
# data[16] = np.rad2deg(data[16])/data[0]
# plt.axhline(y=0, color="black", alpha=0.1)
# plt.plot(data[1], data[14], label="yaw (180 = south, positive ccw???)")  # TODO I alread checked this one is yaw!! but need to check ccw and south
# plt.plot(data[1], data[15], label="right/pitch")  # TODO check order
# plt.plot(data[1], data[16], label="forward/roll")  # TODO check order
# plt.legend()
# plt.show()

plt.title("Suspension travel (normlized) over time (min)\n0 = fully stretched, 1 = fully compressed")
data[17] /= data[0]
data[18] /= data[0]
data[19] /= data[0]
data[20] /= data[0]
plt.axhline(y=0, color="black", alpha=0.1)
plt.axhline(y=1, color="black", alpha=0.1)
plt.plot(data[1], data[17], label="FL")
plt.plot(data[1], data[18], label="FR")
plt.plot(data[1], data[19], label="RL")
plt.plot(data[1], data[20], label="RR")
plt.legend()
plt.show()

# plt.title("Front suspension travel (normlized) over time (min)\n0 = fully stretched, 1 = fully compressed")
# plt.axhline(y=0, color="black", alpha=0.1)
# plt.axhline(y=1, color="black", alpha=0.1)
# plt.plot(data[1], data[17], label="FL")
# plt.plot(data[1], data[18], label="FR")
# plt.legend()
# plt.show()

# plt.title("Rear suspension travel (normlized) over time (min)\n0 = fully stretched, 1 = fully compressed")
# plt.axhline(y=0, color="black", alpha=0.1)
# plt.axhline(y=1, color="black", alpha=0.1)
# plt.plot(data[1], data[19], label="RL")
# plt.plot(data[1], data[20], label="RR")
# plt.legend()
# plt.show()

raise

plt.title("norm. tire slip ratio (0 = max grip)")
plt.axhline(y=0, color="gray")
plt.axhline(y=1, color="gray")
plt.axhline(y=-1, color="gray")
plt.plot(data[1], data[21], label="FL")
plt.plot(data[1], data[22], label="FR")
plt.plot(data[1], data[23], label="RL")
plt.plot(data[1], data[24], label="RR")
plt.legend()
plt.show()


plt.title("wheel rotation speed (rpm)")
plt.axhline(y=0, color="gray")
plt.plot(data[1], data[25]*30/np.pi, label="FL")
plt.plot(data[1], data[26]*30/np.pi, label="FR")
plt.plot(data[1], data[27]*30/np.pi, label="RL")
plt.plot(data[1], data[28]*30/np.pi, label="RR")
plt.legend()
plt.show()

plt.title("wheel rotation speed diff (rpm)")
# plt.plot(data[1], np.abs(data[25]/data[26] - 1), label="Front")
plt.plot(data[1], np.abs(data[27]/data[28] - 1), label="-1")
plt.plot(data[1], 2*np.abs((data[27] - data[28])/(data[27] + data[28])), label="+-")
plt.legend()
plt.show()

# skip wheel rumble 29 30 31 32
# skip wheel puddle 33 34 35 36
# skip surface rumble 37 38 39 40

plt.title("norm. tire slip angle (0 = max grip)")
plt.axhline(y=0, color="gray")
plt.axhline(y=1, color="gray")
plt.axhline(y=-1, color="gray")
plt.plot(data[1], data[41], label="FL")
plt.plot(data[1], data[42], label="FR")
plt.plot(data[1], data[43], label="RL")
plt.plot(data[1], data[44], label="RR")
plt.legend()
plt.show()

plt.title("norm. tire slip combined (0 = max grip)")
plt.axhline(y=0, color="gray")
plt.axhline(y=1, color="gray")
plt.axhline(y=-1, color="gray")
plt.plot(data[1], data[45], label="FL")
plt.plot(data[1], data[46], label="FR")
plt.plot(data[1], data[47], label="RL")
plt.plot(data[1], data[48], label="RR")
plt.legend()
plt.show()

plt.title("suspension travel")
plt.axhline(y=0, color="gray")
plt.plot(data[1], data[49], label="FL")
plt.plot(data[1], data[50], label="FR")
plt.plot(data[1], data[51], label="RL")
plt.plot(data[1], data[52], label="RR")
plt.legend()
plt.show()

# skip car ordinal (id) 53
# skip car class 54
# skip car PI 55
# skip drivetrain 56
# skip num of cylinders 57

plt.title("position")
plt.axhline(y=0, color="gray")
plt.plot(data[1], data[58], label="x")
plt.plot(data[1], data[59], label="y")
plt.plot(data[1], data[60], label="z")
plt.legend()
plt.show()

plt.title("speed (kmph)")
plt.axhline(y=0, color="gray")
plt.plot(data[1], 3.6*data[61])
plt.show()

plt.title("power (ps)")
plt.axhline(y=0, color="gray")
plt.plot(data[1], 1.35962*data[62])
plt.show()

plt.title("torque (Nm)")
plt.axhline(y=0, color="gray")
plt.plot(data[1], data[63])
plt.show()

plt.title("tire temperature")
plt.axhline(y=0, color="gray")
plt.plot(data[1], data[64], label="FL")
plt.plot(data[1], data[65], label="FR")
plt.plot(data[1], data[66], label="RL")
plt.plot(data[1], data[67], label="RR")
plt.legend()
plt.show()
