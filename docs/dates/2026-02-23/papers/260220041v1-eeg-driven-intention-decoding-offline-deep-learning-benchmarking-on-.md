---
layout: default
title: EEG-Driven Intention Decoding: Offline Deep Learning Benchmarking on a Robotic Rover
---

# EEG-Driven Intention Decoding: Offline Deep Learning Benchmarking on a Robotic Rover
**arXiv**：[2602.20041v1](https://arxiv.org/abs/2602.20041) · [PDF](https://arxiv.org/pdf/2602.20041.pdf)  
**作者**：Ghadah Alosaimi, Maha Alsayyari, Yixin Sun, Stamos Katsigiannis, Amir Atapour-Abarghouei, Toby P. Breckon  

**一句话要点**：提出基于深度学习的脑机接口框架，用于离线解码机器人漫游中的驾驶意图

**关键词**：脑机接口, 意图解码, 深度学习基准, 机器人控制, EEG信号处理

## 3 点简述
- 核心问题：脑机接口在真实世界机器人导航中解码用户意图仍具挑战性
- 方法要点：使用卷积、循环和Transformer网络，在多个时间窗口对齐EEG信号与动作
- 实验或效果：ShallowConvNet在动作和意图预测中表现最佳，提供可复现基准

## 摘要（原文）

> Brain-computer interfaces (BCIs) provide a hands-free control modality for mobile robotics, yet decoding user intent during real-world navigation remains challenging. This work presents a brain-robot control framework for offline decoding of driving commands during robotic rover operation. A 4WD Rover Pro platform was remotely operated by 12 participants who navigated a predefined route using a joystick, executing the commands forward, reverse, left, right, and stop. Electroencephalogram (EEG) signals were recorded with a 16-channel OpenBCI cap and aligned with motor actions at Delta = 0 ms and future prediction horizons (Delta > 0 ms). After preprocessing, several deep learning models were benchmarked, including convolutional neural networks, recurrent neural networks, and Transformer architectures. ShallowConvNet achieved the highest performance for both action prediction and intent prediction. By combining real-world robotic control with multi-horizon EEG intention decoding, this study introduces a reproducible benchmark and reveals key design insights for predictive deep learning-based BCI systems.

