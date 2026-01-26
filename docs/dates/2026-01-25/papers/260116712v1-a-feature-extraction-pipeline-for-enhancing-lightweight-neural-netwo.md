---
layout: default
title: A Feature Extraction Pipeline for Enhancing Lightweight Neural Networks in sEMG-based Joint Torque Estimation
---

# A Feature Extraction Pipeline for Enhancing Lightweight Neural Networks in sEMG-based Joint Torque Estimation
**arXiv**：[2601.16712v1](https://arxiv.org/abs/2601.16712) · [PDF](https://arxiv.org/pdf/2601.16712.pdf)  
**作者**：Kartik Chari, Raid Dokhan, Anas Homsi, Niklas Kueper, Elsa Andrea Kirchner  

**一句话要点**：提出基于sEMG的特征提取流程，以增强轻量神经网络在关节扭矩估计中的性能。

**关键词**：表面肌电信号, 关节扭矩估计, 特征提取, 轻量神经网络, 机器人辅助康复

## 3 点简述
- 核心问题：机器人辅助康复中，准确预测用户关节扭矩对个性化辅助至关重要。
- 方法要点：使用8通道表面肌电信号，设计特征提取流程，集成到MLP和TCN模型中进行评估。
- 实验或效果：离线分析显示，该流程使MLP在肘部和肩部扭矩预测上达到与TCN相当的性能，适用于训练数据有限场景。

## 摘要（原文）

> Robot-assisted rehabilitation offers an effective approach, wherein exoskeletons adapt to users' needs and provide personalized assistance. However, to deliver such assistance, accurate prediction of the user's joint torques is essential. In this work, we propose a feature extraction pipeline using 8-channel surface electromyography (sEMG) signals to predict elbow and shoulder joint torques. For preliminary evaluation, this pipeline was integrated into two neural network models: the Multilayer Perceptron (MLP) and the Temporal Convolutional Network (TCN). Data were collected from a single subject performing elbow and shoulder movements under three load conditions (0 kg, 1.10 kg, and 1.85 kg) using three motion-capture cameras. Reference torques were estimated from center-of-mass kinematics under the assumption of static equilibrium. Our offline analyses showed that, with our feature extraction pipeline, MLP model achieved mean RMSE of 0.963 N m, 1.403 N m, and 1.434 N m (over five seeds) for elbow, front-shoulder, and side-shoulder joints, respectively, which were comparable to the TCN performance. These results demonstrate that the proposed feature extraction pipeline enables a simple MLP to achieve performance comparable to that of a network designed explicitly for temporal dependencies. This finding is particularly relevant for applications with limited training data, a common scenario patient care.

