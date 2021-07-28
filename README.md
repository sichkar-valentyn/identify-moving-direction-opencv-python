# Identify object's moving direction with OpenCV and Python
Implementing *ROI selection* and applying *built-in OpenCV algorithms* for object tracking:
- BOOSTING Tracker
- MIL Tracker
- **KCF Tracker** (applied by default)
- CSRT Tracker
- MedianFlow Tracker
- TLD Tracker
- MOSSE Tracker

<br/>

### :scroll: Content
* [Requirements](#requirements)
* [How to use](#how-to-use)
* [Results](#results)
* [Future](#future)

<br/>

### :bulb: <a id="requirements">Requirements</a>
- [x] ```pip install opencv-contrib-python==4.2.0.34```
- [x] ```pip install numpy==1.19.2```
  
<br/>

### :radio_button: <a id="how-to-use">How to use</a>
*Command line argument (the only one):*
- [x] **--video**, default value is **test.mov**

<br/>

*To run (with video by default or with different one):*
- [x] python direction.py
- [x] python direction.py --video test.mov

<br/>

*To select ROI (from the first run):*
- [x] Select a ROI and then press **SPACE** or **ENTER** button
- [x] Cancel the selection process by pressing **'c'** button

<br/>

*To select ROI (during the video):*
- [x] Press and hold (few seconds) **'r'** button
- [x] Select a ROI and then press **SPACE** or **ENTER** button

<br/>

### :white_check_mark: <a id="results">Results</a>
*Screenshots of the best results*

![Train 1](https://github.com/sichkar-valentyn/identify-moving-direction-opencv-python/blob/main/images/train_1.png)
![Train 2](https://github.com/sichkar-valentyn/identify-moving-direction-opencv-python/blob/main/images/train_2.png)
![Train 3](https://github.com/sichkar-valentyn/identify-moving-direction-opencv-python/blob/main/images/train_3.png)

<br/>

*GIF image of the best results*
![Train 1 2 3](https://github.com/sichkar-valentyn/identify-moving-direction-opencv-python/blob/main/images/direction_123.gif)

<br/>


<br/>

### :wavy_dash: <a id="future">Future</a>
- [ ] Experiment with **Optical Flow** algorithms
- [ ] Add **compass** and calculate **angle** of the direction

<br/>


### MIT License
### Copyright (c) 2021 Valentyn N Sichkar
### github.com/sichkar-valentyn
### Reference to:
Valentyn N Sichkar. Identify object's moving direction with OpenCV and Python // GitHub platform
