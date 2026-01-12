---
layout: default
title: Motion Compensation for Real Time Ultrasound Scanning in Robotically Assisted Prostate Biopsy Procedures
---

# Motion Compensation for Real Time Ultrasound Scanning in Robotically Assisted Prostate Biopsy Procedures
**arXiv**：[2601.05661v1](https://arxiv.org/abs/2601.05661) · [PDF](https://arxiv.org/pdf/2601.05661.pdf)  
**作者**：Matija Markulin, Luka Matijević, Luka Siktar, Janko Jurdana, Branimir Caran, Marko Švaco, Filip Šuligoj, Bojan Šekoranja  

**一句话要点**：提出机器人辅助超声扫描系统，通过运动补偿在动态环境中稳定重建前列腺以辅助活检。

**关键词**：机器人辅助手术, 超声扫描, 运动补偿, 前列腺活检, 三维重建, 点云配准

## 3 点简述
- 核心问题：前列腺活检依赖医生经验，操作者依赖性高，需提高精度和可及性。
- 方法要点：开发协作机器人系统，自动扫描前列腺模型，通过运动补偿保持探头与前列腺相对位置恒定。
- 实验或效果：在四种运动场景下验证，平均扫描时间30秒，重建时间3秒，运动补偿延迟≤0.5秒，跟踪误差≤3毫米。

## 摘要（原文）

> Prostate cancer is one of the most common types of cancer in men. Its diagnosis by biopsy requires a high level of expertise and precision from the surgeon, so the results are highly operator-dependent. The aim of this work is to develop a robotic system for assisted ultrasound (US) examination of the prostate, a prebiopsy step that could reduce the dexterity requirements and enable faster, more accurate and more available prostate biopsy. We developed and validated a laboratory setup with a collaborative robotic arm that can autonomously scan a prostate phantom and attached the phantom to a medical robotic arm that mimics the patient's movements. The scanning robot keeps the relative position of the US probe and the prostate constant, ensuring a consistent and robust approach to reconstructing the prostate. To reconstruct the prostate, each slice is segmented to generate a series of prostate contours converted into a 3D point cloud used for biopsy planning. The average scan time of the prostate was 30 s, and the average 3D reconstruction of the prostate took 3 s. We performed four motion scenarios: the phantom was scanned in a stationary state (S), with horizontal motion (H), with vertical motion (V), and with a combination of the two (C). System validation is performed by registering the prostate point cloud reconstructions acquired during different motions (H, V, C) with those obtained in the stationary state. ICP registration with a threshold of 0.8 mm yields mean 83.2\% fitness and 0.35 mm RMSE for S-H registration, 84.1\% fitness and 0.37 mm RMSE for S-V registration and 79.4\% fitness and 0.37 mm RMSE for S-C registration. Due to the elastic and soft material properties of the prostate phantom, the maximum robot tracking error was 3 mm, which can be sufficient for prostate biopsy according to medical literature. The maximum delay in motion compensation was 0.5 s.

