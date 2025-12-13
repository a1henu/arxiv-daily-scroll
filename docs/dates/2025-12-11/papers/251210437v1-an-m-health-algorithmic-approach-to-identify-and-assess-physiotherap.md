---
layout: default
title: An M-Health Algorithmic Approach to Identify and Assess Physiotherapy Exercises in Real Time
---

# An M-Health Algorithmic Approach to Identify and Assess Physiotherapy Exercises in Real Time
**arXiv**：[2512.10437v1](https://arxiv.org/abs/2512.10437) · [PDF](https://arxiv.org/pdf/2512.10437.pdf)  
**作者**：Stylianos Kandylakis, Christos Orfanopoulos, Georgios Siolas, Panayiotis Tsanakas  

**一句话要点**：提出基于移动设备的实时物理治疗运动识别与评估算法框架

**关键词**：姿态估计, 序列匹配, 移动健康, 实时评估, 动态规划

## 3 点简述
- 核心问题：实时识别和评估物理治疗运动，支持远程监督和移动健康应用。
- 方法要点：使用姿态估计网络提取关键点，转换为角度特征，结合轻量分类和动态规划序列匹配。
- 实验或效果：系统在客户端运行，实验验证了方法的有效性和实时性能。

## 摘要（原文）

> This work presents an efficient algorithmic framework for real-time identification, classification, and evaluation of human physiotherapy exercises using mobile devices. The proposed method interprets a kinetic movement as a sequence of static poses, which are estimated from camera input using a pose-estimation neural network. Extracted body keypoints are transformed into trigonometric angle-based features and classified with lightweight supervised models to generate frame-level pose predictions and accuracy scores. To recognize full exercise movements and detect deviations from prescribed patterns, we employ a dynamic-programming scheme based on a modified Levenshtein distance algorithm, enabling robust sequence matching and localization of inaccuracies. The system operates entirely on the client side, ensuring scalability and real-time performance. Experimental evaluation demonstrates the effectiveness of the methodology and highlights its applicability to remote physiotherapy supervision and m-health applications.

