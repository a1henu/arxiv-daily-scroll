---
layout: default
title: EqDeepRx: Learning a Scalable MIMO Receiver
---

# EqDeepRx: Learning a Scalable MIMO Receiver
**arXiv**：[2602.11834v1](https://arxiv.org/abs/2602.11834) · [PDF](https://arxiv.org/pdf/2602.11834.pdf)  
**作者**：Mikko Honkala, Dani Korpi, Elias Raninen, Janne M. J. Huttunen  

**一句话要点**：提出EqDeepRx以解决MIMO接收机中机器学习算法扩展性和可解释性差的问题。

**关键词**：MIMO接收机, 深度学习辅助, 可扩展性, 可解释性, 线性均衡器, 信道估计

## 3 点简述
- 核心问题：传统ML接收机在空间复用阶数增加时扩展性差，且缺乏可解释性和泛化能力。
- 方法要点：通过共享权重的DetectorNN实现近线性复杂度扩展，结合线性均衡器和轻量级DenoiseNN增强处理。
- 实验或效果：在5G/6G仿真中，相比基线提升误码率和频谱效率，支持不同MIMO配置无需重训练。

## 摘要（原文）

> While machine learning (ML)-based receiver algorithms have received a great deal of attention in the recent literature, they often suffer from poor scaling with increasing spatial multiplexing order and lack of explainability and generalization. This paper presents EqDeepRx, a practical deep-learning-aided multiple-input multiple-output (MIMO) receiver, which is built by augmenting linear receiver processing with carefully engineered ML blocks. At the core of the receiver model is a shared-weight DetectorNN that operates independently on each spatial stream or layer, enabling near-linear complexity scaling with respect to multiplexing order. To ensure better explainability and generalization, EqDeepRx retains conventional channel estimation and augments it with a lightweight DenoiseNN that learns frequency-domain smoothing. To reduce the dimensionality of the DetectorNN inputs, the receiver utilizes two linear equalizers in parallel: a linear minimum mean-square error (LMMSE) equalizer with interference-plus-noise covariance estimation and a regularized zero-forcing (RZF) equalizer. The parallel equalized streams are jointly consumed by the DetectorNN, after which a compact DemapperNN produces bit log-likelihood ratios for channel decoding. 5G/6G-compliant end-to-end simulations across multiple channel scenarios, pilot patterns, and inter-cell interference conditions show improved error rate and spectral efficiency over a conventional baseline, while maintaining low-complexity inference and support for different MIMO configurations without retraining.

