import serial
import matplotlib.pyplot as plt
from collections import deque

# Replace 'COM3' with your Arduino port (Windows) or '/dev/ttyACM0' (Linux/macOS)
ser = serial.Serial('COM3', 9600)
distances = deque(maxlen=50)  # keep last 50 readings

plt.ion()
fig, ax = plt.subplots()

while True:
    try:
        line = ser.readline().decode('utf-8').strip()
        distance = float(line)
        distances.append(distance)

        ax.clear()
        ax.plot(distances, marker='o')
        ax.set_ylim(0, 50)
        ax.set_ylabel("Distance (cm)")
        ax.set_title("Live Distance Tracking")
        plt.pause(0.05)

    except ValueError:
        continue
