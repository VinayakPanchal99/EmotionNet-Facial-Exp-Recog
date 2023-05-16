#! /usr/bin/env python

import os
import torch.nn as nn
import torch
import numpy as np
import cv2
import sys
import pickle
import collections
from datetime import datetime

class InvertedBottleneck(nn.Module):
    def __init__(self, in_channels, out_channels, kernel_size, groups):
        super(InvertedBottleneck, self).__init__()
        self.leaky = nn.LeakyReLU(0.2)
        self.conv1 = nn.Sequential(
            nn.Conv2d(in_channels, in_channels, kernel_size=1, stride=1, padding=0, bias=False),
            nn.BatchNorm2d(in_channels))
        self.conv2 = nn.Sequential(
            nn.ReflectionPad2d((kernel_size - 1) // 2),
            nn.Conv2d(in_channels, in_channels, kernel_size=kernel_size, stride=1, padding=0, groups=groups, bias=False),
            nn.BatchNorm2d(in_channels))
        self.conv3 = nn.Sequential(
            nn.Conv2d(in_channels, out_channels, kernel_size=1, stride=1, padding=0, bias=False),
            nn.BatchNorm2d(out_channels))
    
    def forward(self, x):
        m = self.conv2(self.leaky(self.conv1(x)))
        m = x + m
        m = self.leaky(self.conv3(self.leaky(m)))

        return m

class EmotionNet(nn.Module):
    def __init__(self, num_emotions):
        super(EmotionNet, self).__init__()
        self.num_emotions = num_emotions
        self.layer1 = nn.Sequential(
            nn.ReflectionPad2d(1),
            nn.Conv2d(1, 24, 3, 2, bias=False), #24x24
            nn.BatchNorm2d(24),
            nn.LeakyReLU(0.2))
        self.layer2 = InvertedBottleneck(24, 40, 3, 4)#12x12
        self.layer3 = InvertedBottleneck(40, 56, 3, 4)#6x6
        self.layer4 = InvertedBottleneck(56, 72, 3, 4)#6x6
        self.avgpool = nn.AvgPool2d(6, 1, 0)#1x1
        self.layer5 = nn.Linear(72, self.num_emotions)
        self.pool = nn.MaxPool2d(3,2,1)
    
    def forward(self, x):
        x = self.avgpool(self.layer4(self.pool(self.layer3(self.pool(self.layer2(self.layer1(x)))))))
        x = x.reshape(-1, 72)
        x = self.layer5(x)
        
        return x

def loader(path):
    image = np.asarray(cv2.imread(path)).astype(np.uint8)[..., ::-1]    #[BGR --> RGB]
    # image = np.transpose(image, (2,0,1))    # [HWC --> CHW]
    return image.copy()

class detect_expression:
	def __init__(self, save_folder="kivygui", weights="fmps8_consolidated_exp3_5emotions.pkl",
					class_labels = ["Neutral", "Happy", "Surprised", "Sad", "Angry"],
					device='cpu'):

		self.flag = True
		self.save_folder = save_folder
		self.weights = weights
		self.class_labels = class_labels
		self.device = device

	def auto_capture(self, video_feed, save_fig=False):
		save_file = os.path.join(self.save_folder, "emotions.log")
		if not os.path.exists(save_file):
			f = open(save_file, "w+")
			f.close()

		figfolder = os.path.join(self.save_folder, "imgs")
		if save_fig:
			os.mkdir(figfolder, exists_ok=True)

		face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
		classifier = EmotionNet(5)
		with open(self.weights, "rb") as weightfile:
			data = pickle.load(weightfile)
			data = collections.OrderedDict(data)
			classifier.load_state_dict(data)
		classifier.eval()
		openfile = open(save_file, "a")
		count = 0

		try:
			cap = video_feed

			while flag:
				# Grab a single frame of video
				ret, frame = cap.read()
				gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
				faces = face_classifier.detectMultiScale(gray,1.3,5)

				for (x, y, w, h) in faces:
					cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
					roi = gray[y:y+h, x:x+w]
					roi = cv2.resize(roi, (48,48), interpolation=cv2.INTER_AREA)

					if np.sum([roi]) != 0:
						roi = roi.astype('float')/255
						# roi = np.transpose(roi, (2,0,1))[::-1, ...]
						roi = torch.from_numpy(roi.copy()).unsqueeze(0).unsqueeze(0)
						roi = roi.type(torch.FloatTensor).to(self.device)
						roi = (roi - 0.5076) / 0.0647
						with torch.no_grad():
							pred = classifier(roi).squeeze()
						_, ind = torch.max(pred, dim=0)
						label = self.class_labels[ind.item()]
						label_position = (x,y)
						count += 1

						openfile.append(datetime.now() + "\t" + label)
						if save_fig:
							cv2.putText(frame, label, label_position, cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 3)
					else:
						openfile.append(datetime.now() + "\t" + "No Face Found")
						if save_fig:
							cv2.putText(frame, 'No Face Found', (20,60), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 3)

				if save_fig:
					cv2.imwrite(os.path.join(figfolder, str(count) + ".jpg"), frame)

			openfile.close()

		except:
			print("Unexpected error!\n")
			return 0

	def end_auto_capture(self):
		self.flag = False

	def manual_capture(self, image_file):
		if image_file != "pic.png":
			sp = image_file.split("/")
			image_file = sp[-1]
		face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
		classifier = EmotionNet(5)
		with open(self.weights, "rb") as weightfile:
			data = pickle.load(weightfile)
			data = collections.OrderedDict(data)
			classifier.load_state_dict(data)
		classifier.eval()

		frame = loader(image_file)
		frame1 = np.asarray(cv2.imread(image_file)).astype(np.uint8)
		if len(frame.shape) == 3 and frame.shape[-1] != 1:
			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		faces = face_classifier.detectMultiScale(gray,1.3,5)

		for (x, y, w, h) in faces:
			roi = gray[y:y+h, x:x+w]
			roi = cv2.resize(roi, (48,48), interpolation=cv2.INTER_AREA)

			if np.sum([roi]) != 0:
				roi = roi.astype('float')/255
				roi = torch.from_numpy(roi.copy()).unsqueeze(0).unsqueeze(0)
				roi = roi.type(torch.FloatTensor).to(self.device)
				roi = (roi - 0.5076) / 0.0647
				with torch.no_grad():
					pred = classifier(roi).squeeze()
				_, ind = torch.max(pred, dim=0)
				label = self.class_labels[ind.item()]
				label_position = (x,y)

				cv2.putText(frame1, label, label_position, cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 3)
			else:
				cv2.putText(frame1, 'No Face Found', (20,60), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 3)

		
		#cv2.rectangle(frame1, (x,y), (x+w,y+h), (255,0,0), 2)
		cv2.imwrite(image_file, frame1)
		emots = ["Happy", "Sad", "Neutral","Angry","Surprised"]
		for i in range(len(emots)):
			if label == emots[i]:
				return i+1