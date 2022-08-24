# -------------------------------------------------- Serial
serial_execution_samples = [
    {
        "real": "0m7.694s",
        "user": "0m0.225s",
        "sys": "0m0.012s",
    },
    {
        "real": "0m7.366s",
        "user": "0m0.204s",
        "sys": "0m0.015s",
    },
    {
        "real": "0m7.724s",
        "user": "0m0.214s",
        "sys": "0m0.029s",
    },
    {
        "real": "0m7.656s",
        "user": "0m0.193s",
        "sys": "0m0.036s",
    },
    {
        "real": "0m7.565s",
        "user": "0m0.203s",
        "sys": "0m0.029s",
    },
    {
        "real": "0m7.803s",
        "user": "0m0.203s",
        "sys": "0m0.024s",
    },
    {
        "real": "0m7.270s",
        "user": "0m0.144s",
        "sys": "0m0.033s",
    },
    {
        "real": "0m8.062s",
        "user": "0m0.164s",
        "sys": "0m0.007s",
    },
    {
        "real": "0m7.478s",
        "user": "0m0.181s",
        "sys": "0m0.016s",
    },
    {
        "real": "0m7.688s",
        "user": "0m0.191s",
        "sys": "0m0.021s",
    },
]
# -------------------------------------------------- Parallel
parallel_execution_samples = [
    {
        "real": "0m1.021s",
        "user": "0m0.247s",
        "sys": "0m0.054s",
    },
    {
        "real": "0m1.054s",
        "user": "0m0.247s",
        "sys": "0m0.049s",
    },
    {
        "real": "0m2.103s",
        "user": "0m0.221s",
        "sys": "0m0.080s",
    },
    {
        "real": "0m1.166s",
        "user": "0m0.263s",
        "sys": "0m0.047s",
    },
    {
        "real": "0m1.203s",
        "user": "0m0.279s",
        "sys": "0m0.057s",
    },
    {
        "real": "0m1.130s",
        "user": "0m0.243s",
        "sys": "0m0.077s",
    },
    {
        "real": "0m1.007s",
        "user": "0m0.269s",
        "sys": "0m0.021s",
    },
    {
        "real": "0m1.044s",
        "user": "0m0.242s",
        "sys": "0m0.077s",
    },
    {
        "real": "0m1.038s",
        "user": "0m0.262s",
        "sys": "0m0.049s",
    },
    {
        "real": "0m1.074s",
        "user": "0m0.247s",
        "sys": "0m0.074s",
    },
]

# Main
from datetime import datetime
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


def human_2_miliseconds (timestamp):
    canonical_timestamp = timestamp.strip().split('m')
    minutes = int(canonical_timestamp[0])
    mseconds = int(float(canonical_timestamp[-1].split('s')[0]) * 1000)
    total_ms = (minutes * 60000 ) + mseconds
    return total_ms

# print(human_2_unix_timestamp_xform("0m0.123s"))

for sample in serial_execution_samples:
    print(human_2_miliseconds(sample['real']), human_2_miliseconds(sample['user']) , human_2_miliseconds(sample['sys']))
    print(human_2_miliseconds(sample['real']))

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3]);  # Plot some data on the axes.
