---
layout: default
title: Lightweight Test-Time Adaptation for EMG-Based Gesture Recognition
---

# Lightweight Test-Time Adaptation for EMG-Based Gesture Recognition
**arXiv**：[2601.04181v1](https://arxiv.org/abs/2601.04181) · [PDF](https://arxiv.org/pdf/2601.04181.pdf)  
**作者**：Nia Touko, Matthew O A Ellis, Cristiano Capone, Alessio Burrello, Elisa Donati, Luca Manneschi  

**一句话要点**：提出轻量级测试时适应框架，以解决基于肌电信号的手势识别中信号漂移导致的性能下降问题。

**关键词**：肌电信号识别, 测试时适应, 时序卷积网络, 轻量级框架, 信号漂移, 少样本校准

## 3 点简述
- 核心问题：表面肌电信号因电极移位、肌肉疲劳和姿势变化产生漂移，导致模型跨会话性能下降。
- 方法要点：采用时序卷积网络，结合因果自适应批归一化、高斯混合模型对齐与经验回放、元学习三种策略进行实时适应。
- 实验或效果：在NinaPro DB6数据集上显著提升跨会话准确率，经验回放在有限数据下稳定，元学习在少样本校准中表现优异。

## 摘要（原文）

> Reliable long-term decoding of surface electromyography (EMG) is hindered by signal drift caused by electrode shifts, muscle fatigue, and posture changes. While state-of-the-art models achieve high intra-session accuracy, their performance often degrades sharply. Existing solutions typically demand large datasets or high-compute pipelines that are impractical for energy-efficient wearables. We propose a lightweight framework for Test-Time Adaptation (TTA) using a Temporal Convolutional Network (TCN) backbone. We introduce three deployment-ready strategies: (i) causal adaptive batch normalization for real-time statistical alignment; (ii) a Gaussian Mixture Model (GMM) alignment with experience replay to prevent forgetting; and (iii) meta-learning for rapid, few-shot calibration. Evaluated on the NinaPro DB6 multi-session dataset, our framework significantly bridges the inter-session accuracy gap with minimal overhead. Our results show that experience-replay updates yield superior stability under limited data, while meta-learning achieves competitive performance in one- and two-shot regimes using only a fraction of the data required by current benchmarks. This work establishes a path toward robust, "plug-and-play" myoelectric control for long-term prosthetic use.

