---
layout: default
title: EEG Emotion Classification Using an Enhanced Transformer-CNN-BiLSTM Architecture with Dual Attention Mechanisms
---

# EEG Emotion Classification Using an Enhanced Transformer-CNN-BiLSTM Architecture with Dual Attention Mechanisms
**arXiv**：[2602.06411v1](https://arxiv.org/abs/2602.06411) · [PDF](https://arxiv.org/pdf/2602.06411.pdf)  
**作者**：S M Rakib UI Karim, Wenyi Lu, Diponkor Bala, Rownak Ara Rasul, Sean Goggins  

**一句话要点**：提出增强型Transformer-CNN-BiLSTM架构，结合双注意力机制，以提升EEG情感分类性能与鲁棒性。

**关键词**：EEG情感分类, 混合深度学习架构, 注意力机制, 卷积神经网络, 双向长短期记忆网络, 正则化策略

## 3 点简述
- 核心问题：EEG信号高维、噪声多且依赖个体，情感识别面临挑战。
- 方法要点：集成卷积特征提取、双向时序建模和自注意力机制，采用正则化策略防止过拟合。
- 实验或效果：在公开数据集上实现最优分类性能，统计测试验证鲁棒性，特征分析强调通道间关系的重要性。

## 摘要（原文）

> Electroencephalography (EEG)-based emotion recognition plays a critical role in affective computing and emerging decision-support systems, yet remains challenging due to high-dimensional, noisy, and subject-dependent signals. This study investigates whether hybrid deep learning architectures that integrate convolutional, recurrent, and attention-based components can improve emotion classification performance and robustness in EEG data. We propose an enhanced hybrid model that combines convolutional feature extraction, bidirectional temporal modeling, and self-attention mechanisms with regularization strategies to mitigate overfitting. Experiments conducted on a publicly available EEG dataset spanning three emotional states (neutral, positive, and negative) demonstrate that the proposed approach achieves state-of-the-art classification performance, significantly outperforming classical machine learning and neural baselines. Statistical tests confirm the robustness of these performance gains under cross-validation. Feature-level analyses further reveal that covariance-based EEG features contribute most strongly to emotion discrimination, highlighting the importance of inter-channel relationships in affective modeling. These findings suggest that carefully designed hybrid architectures can effectively balance predictive accuracy, robustness, and interpretability in EEG-based emotion recognition, with implications for applied affective computing and human-centered intelligent systems.

