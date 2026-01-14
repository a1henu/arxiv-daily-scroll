---
layout: default
title: Contrastive and Multi-Task Learning on Noisy Brain Signals with Nonlinear Dynamical Signatures
---

# Contrastive and Multi-Task Learning on Noisy Brain Signals with Nonlinear Dynamical Signatures
**arXiv**：[2601.08549v1](https://arxiv.org/abs/2601.08549) · [PDF](https://arxiv.org/pdf/2601.08549.pdf)  
**作者**：Sucheta Ghosh, Zahra Monfared, Felix Dietrich  

**一句话要点**：提出两阶段多任务学习框架，结合去噪、动力学建模和表示学习以分析嘈杂脑电信号。

**关键词**：脑电信号分析, 多任务学习, 去噪自编码器, 非线性动力学, 对比学习, Transformer编码器

## 3 点简述
- 核心问题：脑电信号噪声干扰和动力学特征提取困难，影响解码性能。
- 方法要点：先训练去噪自编码器稳定信号，再用多任务架构进行运动想象分类、混沌判别和对比学习。
- 实验或效果：框架提升鲁棒性和泛化能力，在脑电解码中超越基准和最新方法。

## 摘要（原文）

> We introduce a two-stage multitask learning framework for analyzing Electroencephalography (EEG) signals that integrates denoising, dynamical modeling, and representation learning. In the first stage, a denoising autoencoder is trained to suppress artifacts and stabilize temporal dynamics, providing robust signal representations. In the second stage, a multitask architecture processes these denoised signals to achieve three objectives: motor imagery classification, chaotic versus non-chaotic regime discrimination using Lyapunov exponent-based labels, and self-supervised contrastive representation learning with NT-Xent loss. A convolutional backbone combined with a Transformer encoder captures spatial-temporal structure, while the dynamical task encourages sensitivity to nonlinear brain dynamics. This staged design mitigates interference between reconstruction and discriminative goals, improves stability across datasets, and supports reproducible training by clearly separating noise reduction from higher-level feature learning. Empirical studies show that our framework not only enhances robustness and generalization but also surpasses strong baselines and recent state-of-the-art methods in EEG decoding, highlighting the effectiveness of combining denoising, dynamical features, and self-supervised learning.

