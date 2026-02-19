---
layout: default
title: Image Measurement Method for Automatic Insertion of Forks into Inclined Pallet
---

# Image Measurement Method for Automatic Insertion of Forks into Inclined Pallet
**arXiv**：[2602.16178v1](https://arxiv.org/abs/2602.16178) · [PDF](https://arxiv.org/pdf/2602.16178.pdf)  
**作者**：Nobuyuki Kita, Takuro Kato  

**一句话要点**：提出基于广角摄像头的图像测量方法，以自动控制叉车插入倾斜托盘孔洞。

**关键词**：图像测量, 叉车控制, 托盘倾斜检测, 坐标系校准, 广角摄像头

## 3 点简述
- 核心问题：叉车需精确控制叉子高度、位置和倾斜角度以匹配托盘孔洞，实现自动插入。
- 方法要点：使用广角摄像头测量托盘在相机坐标系中的俯仰倾斜，并校准相机与叉子坐标系。
- 实验或效果：在实验空间中，图像测量误差在安全插入允许范围内，验证了方法有效性。

## 摘要（原文）

> In order to insert a fork into a hole of a pallet by a forklift located in front of a pallet, it is necessary to control the height position, reach position, and tilt angle of the fork to match the position and orientation of the hole of the pallet. In order to make AGF (Autonomous Guided Forklift) do this automatically, we propose an image measurement method to measure the pitch inclination of the pallet in the camera coordinate system from an image obtained by using a wide-angle camera. In addition, we propose an image measurement method to easily acquire the calibration information between the camera coordinate system and the fork coordinate system necessary to apply the measurements in the camera coordinate system to the fork control. In the experiment space, a wide-angle camera was fixed at the backrest of a reach type forklift. The wide-angle images taken by placing a pallet in front of the camera were processed. As a result of evaluating the error by comparing the image measurement value with the hand measurement value when changing the pitch inclination angle of the pallet, the relative height of the pallet and the fork, and whether the pallet is loaded or not, it was confirmed that the error was within the allowable range for safely inserting the fork.

