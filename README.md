# HanDigiSlide
v1.0

## Description
![Capture](https://user-images.githubusercontent.com/100322125/177003355-ad5f1944-778b-457d-b4ab-3e4f5ce5f427.PNG)
HanDigiSlide is designed for presenters who instead of using the keyboard and mouse, they just use the webcam to move their slides back and forward or even draw in them.

Here is little demonstration :

https://user-images.githubusercontent.com/100322125/177003732-315a1da0-bd4a-4346-a3c9-4a84f4a2b9b8.mp4

The user can use either default configuration or customized one :

### Default configuration :
<ol>
  <li><strong>Right</strong> = [0, 0, 0, 0, 1]</li>
  <li><strong>Left</strong> = [1, 0, 0, 0, 0]</li>
  <li><strong>Erase</strong> = [0, 1, 1, 1, 0]</li>
  <li><strong>Change color</strong> = [0, 1, 1, 1, 1]</li>
  <li><strong>Show pointer</strong> = [0, 1, 1, 0, 0]</li>
  <li><strong>Draw</strong> = [0, 1, 0, 0, 0]</li>
  <li><strong>Threshold</strong> = 350</li>
</ol>

### Customized configuration
The user fills the form and clicks on <strong>Process</strong>

![d](https://user-images.githubusercontent.com/100322125/177003887-468b3544-c1b0-46fe-8007-f0b72ecc3926.PNG)


### Paramaters
<ol>
  <li><strong>Right :</strong> go forward</li>
  <li><strong>Left :</strong> go back[0, 0, 0, 0, 1]</li>
  <li><strong>Erase :</strong> delete the last drawing [0, 1, 1, 1, 0]</li>
  <li><strong>Change color :</strong> change the pointer's color [0, 1, 1, 1, 1]</li>
  <li><strong>Show pointer :</strong> show the pointer without drawing [0, 1, 1, 0, 0]</li>
  <li><strong>Draw :</strong> draw on the side</li>
  <li><strong>Threshold :</strong> green line on the cam screen, the following gestures which correspond to "right, left, erase, change color" won't be supported until the center of our hand is above the threshold line.</li>
</ol>

#### Notice
- The user shouldn't forget to choose the <strong>directory</strong> in which he put only his slides in <strong>image format</strong> in the <strong>same hard disk partition</strong> of his application.

- The slides have to be sorted, for example : <strong>1.jpg, 2.jpg, 3.jpg, ...etc</strong>

### Command lines
Follow the steps to execute the program :
<ol>
  <li>Considering you're in the root of the project <strong>presentation_app</strong></li>  
  <li>Open the <strong>terminal</strong> or <strong>cmd</strong></li>
  <li>Change directory to <strong>handDetectorSytem</strong> by typing : <strong>cd handDetectorSytem</strong></li>
  <li>Execute the program <strong>MainWindow.py</strong> by typing : <strong>python MainWindow.py</strong></li>
</ol>
