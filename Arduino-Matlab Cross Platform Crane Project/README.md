# Arduino-Matlab Crane Project

The Arduino-MATLAB Crane Project consists of a color sensor programmed by an Arduino microcontroller, a LEGO Mindstorms robotic arm with a color sensor, three color-coded containers, and several red, orange, and blue LEGO blocks. The Arduino microcontroller is coded using the Arduino programming language while the LEGO Mindstorms robotic arm is coded using MATLAB.

The color sensor that is connected to the Arduino microcontroller is positioned in front of the robotic arm. Red, orange, and blue containers are placed around the robotic arm. A LEGO block is placed directly underneath the arm. When a button connected to the Arduino microcontroller is clicked, the color sensor detects the color of the LEGO block and sends a signal to the LEGO Mindstorms robotic arm via the Arduino microcontroller Serial port.

The robotic arm receives the signal through MATLAB, causing its color sensor to scan for a container with the same color as the LEGO block. The robotic arm picks up the block and drops it into the container. Finally, the arm moves back to its original position.
