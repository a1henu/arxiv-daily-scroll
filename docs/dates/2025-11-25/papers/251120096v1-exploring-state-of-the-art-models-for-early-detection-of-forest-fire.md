---
layout: default
title: Exploring State-of-the-art models for Early Detection of Forest Fires
---

# Exploring State-of-the-art models for Early Detection of Forest Fires
**arXiv**：[2511.20096v1](https://arxiv.org/abs/2511.20096) · [PDF](https://arxiv.org/pdf/2511.20096.pdf)  
**作者**：Sharjeel Ahmed, Daim Armaghan, Fatima Naweed, Umair Yousaf, Ahmad Zubair, Murtaza Taj  

**一句话要点**：提出合成数据集与模型比较方法以改进森林火灾早期检测

**关键词**：森林火灾检测, 合成数据集, YOLOv7, 检测变换器, 图像分类, 目标定位

## 3 点简述
- 核心问题：现有方法因数据集不足和模型未优化导致漏检，影响早期火灾检测。
- 方法要点：利用游戏模拟器合成包含烟雾和初始火灾图像的数据集，并整合公开图像。
- 实验或效果：在数据集上比较YOLOv7和检测变换器模型，评估分类与定位性能。

## 摘要（原文）

> There have been many recent developments in the use of Deep Learning Neural Networks for fire detection. In this paper, we explore an early warning system for detection of forest fires. Due to the lack of sizeable datasets and models tuned for this task, existing methods suffer from missed detection. In this work, we first propose a dataset for early identification of forest fires through visual analysis. Unlike existing image corpuses that contain images of wide-spread fire, our dataset consists of multiple instances of smoke plumes and fire that indicates the initiation of fire. We obtained this dataset synthetically by utilising game simulators such as Red Dead Redemption 2. We also combined our dataset with already published images to obtain a more comprehensive set. Finally, we compared image classification and localisation methods on the proposed dataset. More specifically we used YOLOv7 (You Only Look Once) and different models of detection transformer.

