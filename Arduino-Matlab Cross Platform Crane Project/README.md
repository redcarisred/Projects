# Arduino-Matlab Crane Project

In the Arduino-Matlab Crane Project, there is a color sensor attached to an Arduino microcontroller, a LEGO Mindstorms robotic arm and color sensor programmed with MATLAB, three color-coded containers, and several red, orange, and blue LEGO blocks. 

The color sensor is positioned in front of the robotic arm. Red, orange, and blue containers are placed around the robotic arm. A LEGO block is placed directly underneath the arm. When a button is clicked, the color sensor detects the color of the LEGO block and sends a signal to the LEGO Mindstorms robotic arm.

The robotic arm recieves the signal and causes a built-in moving color sensor to start searching for a container with the same color as the LEGO block. When the container is found, the robotic arm picks up the block and drops it into the same-colored container. 

Then the arm moves back to its original position, and the scripts resets.
