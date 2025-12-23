---
layout: default
title: Sign Language Recognition using Parallel Bidirectional Reservoir Computing
---

# Sign Language Recognition using Parallel Bidirectional Reservoir Computing
**arXiv**：[2512.19451v1](https://arxiv.org/abs/2512.19451) · [PDF](https://arxiv.org/pdf/2512.19451.pdf)  
**作者**：Nitin Kumar Singh, Arie Rachmad Syulistyo, Yuichiro Tanaka, Hakaru Tamukoh  

**一句话要点**：提出并行双向储层计算结合MediaPipe的轻量级手语识别系统，以解决边缘设备实时部署问题。

**关键词**：手语识别, 储层计算, 边缘计算, 实时处理, 轻量级模型, 时间序列分析

## 3 点简述
- 核心问题：基于深度学习的手语识别模型计算资源需求高，难以在边缘设备实时部署。
- 方法要点：使用MediaPipe实时提取手部关节坐标，并行双向储层计算架构捕获时间依赖以生成丰富特征。
- 实验或效果：在WLASL数据集上实现最高91.74%准确率，训练时间大幅减少至18.67秒，适合边缘设备。

## 摘要（原文）

> Sign language recognition (SLR) facilitates communication between deaf and hearing communities. Deep learning based SLR models are commonly used but require extensive computational resources, making them unsuitable for deployment on edge devices. To address these limitations, we propose a lightweight SLR system that combines parallel bidirectional reservoir computing (PBRC) with MediaPipe. MediaPipe enables real-time hand tracking and precise extraction of hand joint coordinates, which serve as input features for the PBRC architecture. The proposed PBRC architecture consists of two echo state network (ESN) based bidirectional reservoir computing (BRC) modules arranged in parallel to capture temporal dependencies, thereby creating a rich feature representation for classification. We trained our PBRC-based SLR system on the Word-Level American Sign Language (WLASL) video dataset, achieving top-1, top-5, and top-10 accuracies of 60.85%, 85.86%, and 91.74%, respectively. Training time was significantly reduced to 18.67 seconds due to the intrinsic properties of reservoir computing, compared to over 55 minutes for deep learning based methods such as Bi-GRU. This approach offers a lightweight, cost-effective solution for real-time SLR on edge devices.

