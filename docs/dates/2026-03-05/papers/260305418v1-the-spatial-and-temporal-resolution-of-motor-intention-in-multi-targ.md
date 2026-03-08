---
layout: default
title: The Spatial and Temporal Resolution of Motor Intention in Multi-Target Prediction
---

# The Spatial and Temporal Resolution of Motor Intention in Multi-Target Prediction
**arXiv**：[2603.05418v1](https://arxiv.org/abs/2603.05418) · [PDF](https://arxiv.org/pdf/2603.05418.pdf)  
**作者**：Marie Dominique Schmidt, Ioannis Iossifidis  

**一句话要点**：提出基于肌电信号的多目标运动意图预测方法，以提升康复辅助系统的响应性。

**关键词**：运动意图解码, 肌电信号分析, 多目标预测, 康复辅助技术, 时间空间分辨率

## 3 点简述
- 核心问题：解码人类运动意图，特别是从肌电信号预测运动方向和目标位置。
- 方法要点：结合数据驱动时间分割与随机森林、卷积神经网络分类器分析肌电数据。
- 实验或效果：在25个空间目标上，随机森林准确率达80%，卷积神经网络达75%。

## 摘要（原文）

> Reaching for grasping, and manipulating objects are essential motor functions in everyday life. Decoding human motor intentions is a central challenge for rehabilitation and assistive technologies. This study focuses on predicting intentions by inferring movement direction and target location from multichannel electromyography (EMG) signals, and investigating how spatially and temporally accurate such information can be detected relative to movement onset. We present a computational pipeline that combines data-driven temporal segmentation with classical and deep learning classifiers in order to analyse EMG data recorded during the planning, early execution, and target contact phases of a delayed reaching task.
>   Early intention prediction enables devices to anticipate user actions, improving responsiveness and supporting active motor recovery in adaptive rehabilitation systems. Random Forest achieves $80\%$ accuracy and Convolutional Neural Network $75\%$ accuracy across $25$ spatial targets, each separated by $14^\circ$ azimuth/altitude. Furthermore, a systematic evaluation of EMG channels, feature sets, and temporal windows demonstrates that motor intention can be efficiently decoded even with drastically reduced data. This work sheds light on the temporal and spatial evolution of motor intention, paving the way for anticipatory control in adaptive rehabilitation systems and driving advancements in computational approaches to motor neuroscience.

