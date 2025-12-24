---
layout: default
title: AUDRON: A Deep Learning Framework with Fused Acoustic Signatures for Drone Type Recognition
---

# AUDRON: A Deep Learning Framework with Fused Acoustic Signatures for Drone Type Recognition
**arXiv**：[2512.20407v1](https://arxiv.org/abs/2512.20407) · [PDF](https://arxiv.org/pdf/2512.20407.pdf)  
**作者**：Rajdeep Chatterjee, Sudip Chakrabarty, Trishaani Acharjee, Deepanjali Mishra  

**一句话要点**：提出AUDRON混合深度学习框架，通过融合声学特征实现无人机类型识别，适用于安全监控场景。

**关键词**：无人机识别, 声学传感, 特征融合, 深度学习, 卷积神经网络, 自编码器

## 3 点简述
- 核心问题：无人机滥用引发安全风险，需低成本非侵入式检测机制。
- 方法要点：结合MFCC和STFT特征，使用CNN、循环层和自编码器进行融合与分类。
- 实验或效果：在二元和多类分类中分别达到98.51%和97.11%准确率，展现良好泛化能力。

## 摘要（原文）

> Unmanned aerial vehicles (UAVs), commonly known as drones, are increasingly used across diverse domains, including logistics, agriculture, surveillance, and defense. While these systems provide numerous benefits, their misuse raises safety and security concerns, making effective detection mechanisms essential. Acoustic sensing offers a low-cost and non-intrusive alternative to vision or radar-based detection, as drone propellers generate distinctive sound patterns. This study introduces AUDRON (AUdio-based Drone Recognition Network), a hybrid deep learning framework for drone sound detection, employing a combination of Mel-Frequency Cepstral Coefficients (MFCC), Short-Time Fourier Transform (STFT) spectrograms processed with convolutional neural networks (CNNs), recurrent layers for temporal modeling, and autoencoder-based representations. Feature-level fusion integrates complementary information before classification. Experimental evaluation demonstrates that AUDRON effectively differentiates drone acoustic signatures from background noise, achieving high accuracy while maintaining generalizability across varying conditions. AUDRON achieves 98.51 percent and 97.11 percent accuracy in binary and multiclass classification. The results highlight the advantage of combining multiple feature representations with deep learning for reliable acoustic drone detection, suggesting the framework's potential for deployment in security and surveillance applications where visual or radar sensing may be limited.

