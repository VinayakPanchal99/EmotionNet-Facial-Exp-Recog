# EmotionNet-Facial-Expression-Recognition

The project is facial-expression-recognition system using ResNext to identify a person's emotions and send mood feedback report/detailed mood analysis report to make him/her joyful. The project classifies the person’s emotions into five categories: happy, sad, angry, surprised, and neutral. For more detail you can refer our research paper: [EmotionNet: ResNeXt Inspired CNN Architecture for Emotion Analysis on Raspberry Pi](https://ieeexplore.ieee.org/document/9573569)

The classifier network was trained on the FERPlus dataset. An interactive GUI platform was designed using KivyMD to control the overall system. 


## Requirements

+ PyTorch
+ OpenCV
+ Kivy==2.2.0rc1: [Kivy](https://kivy.org/doc/stable/gettingstarted/installation.html) 
+ [KivyMD](https://github.com/kivymd/KivyMD)
+ [ReportLab](https://docs.reportlab.com/install/open_source_installation/)

## Steps to Run

STEP 1: Install Kivy and KivyMD in virtual environment. Install PyTorch, OpenCV and ReportLab on your system

STEP 2: Now that you have installed the necessary libraries, next step is clone the repo and place it in the same folder where you installed kivy and kivyMD. All files should be in same folder as shown 
![](https://github.com/VinayakPanchal99/EmotionNet-Facial-Exp-Recog/blob/main/Screenshot/2023-05-15%20(1).png)

STEP 3: How to run code: First get into the above working directory using commmand line and then activate the virtual environment. 
```
source kivy_venv/Scripts/activate
```
Then run the below code:
```
python allcode.py
```

## Project pics
![](https://github.com/VinayakPanchal99/EmotionNet-Facial-Exp-Recog/blob/main/Screenshot/Loginpage.png)
![](https://github.com/VinayakPanchal99/EmotionNet-Facial-Exp-Recog/blob/main/Screenshot/Capturepage.png)
![](https://github.com/VinayakPanchal99/EmotionNet-Facial-Exp-Recog/blob/main/Screenshot/manualcap.png)
![](https://github.com/VinayakPanchal99/EmotionNet-Facial-Exp-Recog/blob/main/Screenshot/autocap.png)
![](https://github.com/VinayakPanchal99/EmotionNet-Facial-Exp-Recog/blob/main/Screenshot/pics%20senti.png)
![](https://github.com/VinayakPanchal99/EmotionNet-Facial-Exp-Recog/blob/main/images/image_9.jpg)
![](https://github.com/VinayakPanchal99/EmotionNet-Facial-Exp-Recog/blob/main/pic.png)

## Reference

 - [FAST-FACE-EXP by codedev99](https://github.com/codedev99/fast-face-exp)
 - [EmotionNet: ResNeXt Inspired CNN Architecture for Emotion Analysis on Raspberry Pi](https://ieeexplore.ieee.org/document/9573569)


