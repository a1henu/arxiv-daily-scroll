---
layout: default
title: Energy-Efficient Fast Object Detection on Edge Devices for IoT Systems
---

# Energy-Efficient Fast Object Detection on Edge Devices for IoT Systems
**arXiv**：[2602.09515v1](https://arxiv.org/abs/2602.09515) · [PDF](https://arxiv.org/pdf/2602.09515.pdf)  
**作者**：Mas Nurul Achmadiah, Afaroj Ahamad, Chi-Chia Sun, Wen-Kai Kuo  

**一句话要点**：提出基于帧差法的轻量检测算法，以提升物联网边缘设备上快速目标检测的能效与准确性。

**关键词**：物联网系统, 边缘计算, 快速目标检测, 帧差法, 能效优化, 轻量算法

## 3 点简述
- 核心问题：物联网系统需高效能快速目标检测，端到端方法在能效和速度上不足。
- 方法要点：采用帧差法结合AI分类器，在边缘设备上实现轻量级检测，优化计算效率。
- 实验或效果：相比端到端方法，平均准确率提升28.314%，能效提高3.6倍，延迟降低39.305%。

## 摘要（原文）

> This paper presents an Internet of Things (IoT) application that utilizes an AI classifier for fast-object detection using the frame difference method. This method, with its shorter duration, is the most efficient and suitable for fast-object detection in IoT systems, which require energy-efficient applications compared to end-to-end methods. We have implemented this technique on three edge devices: AMD AlveoT M U50, Jetson Orin Nano, and Hailo-8T M AI Accelerator, and four models with artificial neural networks and transformer models. We examined various classes, including birds, cars, trains, and airplanes. Using the frame difference method, the MobileNet model consistently has high accuracy, low latency, and is highly energy-efficient. YOLOX consistently shows the lowest accuracy, lowest latency, and lowest efficiency. The experimental results show that the proposed algorithm has improved the average accuracy gain by 28.314%, the average efficiency gain by 3.6 times, and the average latency reduction by 39.305% compared to the end-to-end method. Of all these classes, the faster objects are trains and airplanes. Experiments show that the accuracy percentage for trains and airplanes is lower than other categories. So, in tasks that require fast detection and accurate results, end-to-end methods can be a disaster because they cannot handle fast object detection. To improve computational efficiency, we designed our proposed method as a lightweight detection algorithm. It is well suited for applications in IoT systems, especially those that require fast-moving object detection and higher accuracy.

