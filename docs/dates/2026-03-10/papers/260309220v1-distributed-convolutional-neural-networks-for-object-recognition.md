---
layout: default
title: Distributed Convolutional Neural Networks for Object Recognition
---

# Distributed Convolutional Neural Networks for Object Recognition
**arXiv**：[2603.09220v1](https://arxiv.org/abs/2603.09220) · [PDF](https://arxiv.org/pdf/2603.09220.pdf)  
**作者**：Liang Sun  

**一句话要点**：提出分布式卷积神经网络以解决特定正类识别问题

**关键词**：分布式卷积神经网络, 特定类识别, 损失函数设计, 特征解耦, 轻量化模型, 目标检测

## 3 点简述
- 核心问题：如何从复杂背景中仅识别特定正类，避免负类特征干扰。
- 方法要点：设计新损失函数，将正类样本映射到高维空间紧凑集，负类映射到原点。
- 实验或效果：模型轻量化，泛化能力强，对未见类有效，简化目标检测任务。

## 摘要（原文）

> This paper proposes a novel loss function for training a distributed convolutional neural network (DisCNN) to recognize only a specific positive class. By mapping positive samples to a compact set in high-dimensional space and negative samples to Origin, the DisCNN extracts only the features of the positive class. An experiment is given to prove this. Thus, the features of the positive class are disentangled from those of the negative classes. The model has a lightweight architecture because only a few positive-class features need to be extracted. The model demonstrates excellent generalization on the test data and remains effective even for unseen classes. Finally, using DisCNN, object detection of positive samples embedded in a large and complex background is straightforward.

