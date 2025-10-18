---
layout: default
title: EdgeNavMamba: Mamba Optimized Object Detection for Energy Efficient Edge Devices
---

# EdgeNavMamba: Mamba Optimized Object Detection for Energy Efficient Edge Devices
**arXiv**：[2510.14946v1](https://arxiv.org/abs/2510.14946) · [PDF](https://arxiv.org/pdf/2510.14946.pdf)  
**作者**：Romina Aalishah, Mozhgan Navardi, Tinoosh Mohsenin  

**一句话要点**：提出EdgeNavMamba框架，结合Mamba目标检测与强化学习，优化边缘设备上的自主导航。

**关键词**：边缘计算, 目标检测, 强化学习, 模型压缩, 自主导航, Mamba模型

## 3 点简述
- 边缘设备计算资源受限，需高效深度学习模型支持实时自主导航。
- 使用强化学习框架，集成Mamba目标检测器提取边界框，驱动导航策略。
- 实验显示模型尺寸减少67%，能耗降低73%，导航成功率超90%。

## 摘要（原文）

> Deployment of efficient and accurate Deep Learning models has long been a
> challenge in autonomous navigation, particularly for real-time applications on
> resource-constrained edge devices. Edge devices are limited in computing power
> and memory, making model efficiency and compression essential. In this work, we
> propose EdgeNavMamba, a reinforcement learning-based framework for
> goal-directed navigation using an efficient Mamba object detection model. To
> train and evaluate the detector, we introduce a custom shape detection dataset
> collected in diverse indoor settings, reflecting visual cues common in
> real-world navigation. The object detector serves as a pre-processing module,
> extracting bounding boxes (BBOX) from visual input, which are then passed to an
> RL policy to control goal-oriented navigation. Experimental results show that
> the student model achieved a reduction of 67% in size, and up to 73% in energy
> per inference on edge devices of NVIDIA Jetson Orin Nano and Raspberry Pi 5,
> while keeping the same performance as the teacher model. EdgeNavMamba also
> maintains high detection accuracy in MiniWorld and IsaacLab simulators while
> reducing parameters by 31% compared to the baseline. In the MiniWorld
> simulator, the navigation policy achieves over 90% success across environments
> of varying complexity.

