---
layout: default
title: Feature Coding for Scalable Machine Vision
---

# Feature Coding for Scalable Machine Vision
**arXiv**：[2512.10209v1](https://arxiv.org/abs/2512.10209) · [PDF](https://arxiv.org/pdf/2512.10209.pdf)  
**作者**：Md Eimran Hossain Eimon, Juan Merlos, Ashan Perera, Hari Kalva, Velibor Adzic, Borko Furht  

**一句话要点**：提出特征编码测试模型以解决边缘-云协同推理中的带宽挑战

**关键词**：特征编码, 边缘计算, 带宽优化, 机器视觉, 标准制定

## 3 点简述
- 核心问题：深度神经网络在边缘设备部署时面临高计算需求，传统方法在延迟、带宽和隐私间存在权衡
- 方法要点：基于MPEG特征编码标准，设计压缩中间特征的比特流语法和编解码器管道
- 实验或效果：在多个视觉任务中实现平均85.14%的比特率降低，同时保持准确性

## 摘要（原文）

> Deep neural networks (DNNs) drive modern machine vision but are challenging to deploy on edge devices due to high compute demands. Traditional approaches-running the full model on-device or offloading to the cloud face trade-offs in latency, bandwidth, and privacy. Splitting the inference workload between the edge and the cloud offers a balanced solution, but transmitting intermediate features to enable such splitting introduces new bandwidth challenges. To address this, the Moving Picture Experts Group (MPEG) initiated the Feature Coding for Machines (FCM) standard, establishing a bitstream syntax and codec pipeline tailored for compressing intermediate features. This paper presents the design and performance of the Feature Coding Test Model (FCTM), showing significant bitrate reductions-averaging 85.14%-across multiple vision tasks while preserving accuracy. FCM offers a scalable path for efficient and interoperable deployment of intelligent features in bandwidth-limited and privacy-sensitive consumer applications.

