---
layout: default
title: PTS-SNN: A Prompt-Tuned Temporal Shift Spiking Neural Networks for Efficient Speech Emotion Recognition
---

# PTS-SNN: A Prompt-Tuned Temporal Shift Spiking Neural Networks for Efficient Speech Emotion Recognition
**arXiv**：[2602.08240v1](https://arxiv.org/abs/2602.08240) · [PDF](https://arxiv.org/pdf/2602.08240.pdf)  
**作者**：Xun Su, Huamin Wang, Qi Zhang  

**一句话要点**：提出PTS-SNN框架，通过提示调优对齐SSL与SNN，实现高效语音情感识别。

**关键词**：语音情感识别, 脉冲神经网络, 自监督学习, 提示调优, 能效优化

## 3 点简述
- 核心问题：SSL表示与SNN分布不匹配，导致神经元编码能力下降。
- 方法要点：引入时序移位编码器和上下文感知膜电位校准，动态调节神经元偏置。
- 实验效果：在IEMOCAP等数据集上达到73.34%准确率，参数和能耗显著降低。

## 摘要（原文）

> Speech Emotion Recognition (SER) is widely deployed in Human-Computer Interaction, yet the high computational cost of conventional models hinders their implementation on resource-constrained edge devices. Spiking Neural Networks (SNNs) offer an energy-efficient alternative due to their event-driven nature; however, their integration with continuous Self-Supervised Learning (SSL) representations is fundamentally challenged by distribution mismatch, where high-dynamic-range embeddings degrade the information coding capacity of threshold-based neurons. To resolve this, we propose Prompt-Tuned Spiking Neural Networks (PTS-SNN), a parameter-efficient neuromorphic adaptation framework that aligns frozen SSL backbones with spiking dynamics. Specifically, we introduce a Temporal Shift Spiking Encoder to capture local temporal dependencies via parameter-free channel shifts, establishing a stable feature basis. To bridge the domain gap, we devise a Context-Aware Membrane Potential Calibration strategy. This mechanism leverages a Spiking Sparse Linear Attention module to aggregate global semantic context into learnable soft prompts, which dynamically regulate the bias voltages of Parametric Leaky Integrate-and-Fire (PLIF) neurons. This regulation effectively centers the heterogeneous input distribution within the responsive firing range, mitigating functional silence or saturation. Extensive experiments on five multilingual datasets (e.g., IEMOCAP, CASIA, EMODB) demonstrate that PTS-SNN achieves 73.34\% accuracy on IEMOCAP, comparable to competitive Artificial Neural Networks (ANNs), while requiring only 1.19M trainable parameters and 0.35 mJ inference energy per sample.

