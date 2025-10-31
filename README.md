# DistanceTracker
A project with Arduino and Python that measures the distance in real time and will show it through an updating graph

## Setup
1. **Arduino Setup**
   1. Connect an ultrasonic sensor: TRIG → pin 9, ECHO → pin 10.
   2. Open `distance_tracker.ino` in the Arduino IDE.
   3. Upload the sketch to your Arduino board.

2. **Python Visualization Setup**
   1. Install dependencies:
      ```bash
      pip install pyserial matplotlib
      ```
   2. Update the `COM` port in `visualize_distance.py` to match your Arduino.
   3. Run the Python script:
      ```bash
      python visualize_distance.py
      ```
